from database.DB_connect import DBConnect
from model.arco import Arco
from model.driver import Driver


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select year from seasons s """
        cursor.execute(query)
        for row in cursor:
            result.append(row["year"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllDrivers():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select * from drivers d"""
        cursor.execute(query)
        for row in cursor:
            result.append(Driver(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select distinct d.*
                    from races r , results r2 , status s , drivers d 
                    where r.raceId = r2.raceId and r2.driverId = d.driverId
                    and r.`year` = %s
                    and r2.`position` is not null"""
        cursor.execute(query, (year, ))
        for row in cursor:
            result.append(Driver(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(year, idMapDrivers):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        result = []
        query = """select t1.driverid as d1, t1.`position` as p1, t1.raceid , t2.driverid as d2, t2.`position` as p2
                    from (select d.driverId, d.forename, d.surname, r2.`position`,  r.`date`, r.raceId
		                    from drivers d , results r2 , races r 
		                    where d.driverId = r2.driverId  and r2.raceId = r.raceId 
		                    and r.`year` = %s
		                    and r2.`position` is not null
		                    order by r.raceId )	as t1
                    left join (select d.driverId, d.forename, d.surname, r2.`position`,  r.`date`, r.raceId
			                from drivers d , results r2 , races r 
			                where d.driverId = r2.driverId  and r2.raceId = r.raceId 
			                and r.`year` = %s
			                and r2.`position` is not null
			        order by r.raceId ) as t2
                    on t1.raceid = t2.raceid
                    where t1.`position`<t2.`position`"""
        cursor.execute(query, (year, year, ))
        for row in cursor:
            result.append(Arco(idMapDrivers[row["d1"]], row["p1"], row["raceId"], idMapDrivers[row["d2"]], row["p2"]))
        cursor.close()
        conn.close()
        return result


if __name__ == "__main__":
    print(DAO.getAllYears())

