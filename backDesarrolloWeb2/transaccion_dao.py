from base_dao import BaseDAO
from models import Transaccion

class TransaccionDAO(BaseDAO):

    @staticmethod
    def get_all():
        try:
            query = "SELECT * FROM Transaccion"
            results = BaseDAO.execute_query(query, fetch=True)
            print("Resultados de la consulta:")
            return [Transaccion(**{k.lower(): v for k, v in row.items()}) for row in results] if results else []
        except Exception as e:
            print(f"Error obteniendo las transacciones: {e}")
            return []

    @staticmethod
    def insert(transaccion):
        try:
            query = "INSERT INTO Transaccion (IdUsuario, Tipo, Monto) VALUES (%s, %s, %s)"
            values = (transaccion.idusuario, transaccion.tipo, transaccion.monto)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Transacción agregada correctamente.")
            return rows
        except Exception as e:
            print(f"Error insertando la transacción: {e}")
            return 0

    @staticmethod
    def update(transaccion):
        try:
            query = "UPDATE Transaccion SET IdUsuario=%s, Tipo=%s, Monto=%s WHERE Id=%s"
            values = (transaccion.idusuario, transaccion.tipo, transaccion.monto, transaccion.id)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Transacción actualizada correctamente.")
            return rows
        except Exception as e:
            print(f"Error actualizando la transacción: {e}")
            return 0

    @staticmethod
    def delete(transaccion_id):
        try:
            query = "DELETE FROM Transaccion WHERE Id=%s"
            values = (transaccion_id,)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Transacción eliminada correctamente.")
            return rows
        except Exception as e:
            print(f"Error eliminando la transacción: {e}")
            return 0
