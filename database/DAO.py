from database.DB_connect import DBConnect
from model.connection import Connection


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_years():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """
                select distinct year(datetime) as year from sighting
                """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["year"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_shapes(year):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """
                select distinct shape as shape 
                from sighting
                where year(datetime) = %s
                """
        cursor.execute(query, (year, ))
        result = []
        for row in cursor:
            result.append(row["shape"])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_connections(year, shape):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        print(f"DAO year: {year}, shape: {shape}")
        query = """
                select n.state1, n.state2, count(*) as peso 
                from neighbor n left join sighting s1 
                on  year(s1.datetime) = 2010 and s1.state = n.state1
                left join sighting s2 
                on year(s2.datetime) = 2010 and s2.state = n.state2
                and ABS(datediff(s1.datetime, s2.datetime)) <= 1 
                where n.state1 < n.state2 
                group by n.state1, n.state2
                """
        cursor.execute(query, (year, shape, year, shape, ))
        result = []
        for row in cursor:
            result.append(Connection(row["state1"], row["state2"], row["sightings"]))

        print(f"DAO get connections: {result}")
        cursor.close()
        cnx.close()
        return result

