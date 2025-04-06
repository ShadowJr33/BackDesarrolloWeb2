from conection import Connection

class BaseDAO:
    
    @staticmethod
    def execute_query(query, values=None, fetch=False, fetch_one=False):
        
        connection = None
        try:
            connection = Connection.get_connection1()
            cursor = connection.cursor(dictionary=True)  # Devuelve un diccionario en lugar de tuplas
            cursor.execute(query, values)
            
            if fetch:
                return cursor.fetchall() if not fetch_one else cursor.fetchone()
            else:
                connection.commit()
                return cursor.rowcount

        except Exception as e:
            print(f'Error executing query: {e}')
        finally:
            if connection is not None:
                cursor.close()
                Connection.releaseConnection(connection)
