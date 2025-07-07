from database.DB_connect import DBConnect


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


if __name__ == "__main__":
    print(DAO.getAllYears())

