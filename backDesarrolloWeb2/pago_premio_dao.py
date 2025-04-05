from base_dao import BaseDAO
from models import PagoPremio

class PagoPremioDAO(BaseDAO):

    @staticmethod
    def get_all():
        try:
            query = "SELECT * FROM PagoPremio"
            results = BaseDAO.execute_query(query, fetch=True)
            print("Resultados de la consulta:")
            return [PagoPremio(**{k.lower(): v for k, v in row.items()}) for row in results] if results else []
        except Exception as e:
            print(f"Error obteniendo los pagos de premio: {e}")
            return []

    @staticmethod
    def insert(pago_premio):
        try:
            query = "INSERT INTO PagoPremio (IdUsuario, IdRifa_Apuesta, ValorGanado) VALUES (%s, %s, %s)"
            values = (pago_premio.idusuario, pago_premio.idrifa_apuesta, pago_premio.valorganado)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Pago de premio agregado correctamente.")
            return rows
        except Exception as e:
            print(f"Error insertando el pago de premio: {e}")
            return 0

    @staticmethod
    def update(pago_premio):
        try:
            query = "UPDATE PagoPremio SET IdUsuario=%s, IdRifa_Apuesta=%s, ValorGanado=%s WHERE Id=%s"
            values = (pago_premio.idusuario, pago_premio.idrifa_apuesta, pago_premio.valorganado, pago_premio.id)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Pago de premio actualizado correctamente.")
            return rows
        except Exception as e:
            print(f"Error actualizando el pago de premio: {e}")
            return 0

    @staticmethod
    def delete(pago_premio_id):
        try:
            query = "DELETE FROM PagoPremio WHERE Id=%s"
            values = (pago_premio_id,)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Pago de premio eliminado correctamente.")
            return rows
        except Exception as e:
            print(f"Error eliminando el pago de premio: {e}")
            return 0
