from database.DB_connect import DBConnect
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
                    and r.`year` = %s"""
        cursor.execute(query, (year, ))
        for row in cursor:
            result.append(Driver(**row))
        cursor.close()
        conn.close()
        return result


if __name__ == "__main__":
    print(DAO.getAllYears())

