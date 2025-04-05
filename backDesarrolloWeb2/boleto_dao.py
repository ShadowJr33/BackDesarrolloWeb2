from base_dao import BaseDAO
from models import Boleto

class BoletoDAO(BaseDAO):
    @staticmethod
    def get_all():
        try:
            query = "SELECT * FROM Boleto"
            results = BaseDAO.execute_query(query, fetch=True)
            return [Boleto(**{
                'id': row['Id'],
                'id_rifa': row['IdRifa'],
                'id_usuario': row['IdUsuario'],
                'numero_asignado': row['NumeroAsignado']
            }) for row in results] if results else []
        except Exception as e:
            print(f"Error obteniendo los boletos: {e}")
            return []

    @staticmethod
    def insert(boleto):
        try:
            query = "INSERT INTO Boleto (NumeroAsignado, IdUsuario, IdRifa) VALUES (%s, %s, %s)"
            values = (boleto.numero_asignado, boleto.id_usuario, boleto.id_rifa)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Boleto agregado correctamente.")
            return rows
        except Exception as e:
            print(f"Error insertando el boleto: {e}")
            return 0

    @staticmethod
    def update(boleto):
        try:
            query = "UPDATE Boleto SET NumeroAsignado=%s, IdUsuario=%s, IdRifa=%s WHERE Id=%s"
            values = (boleto.numero_asignado, boleto.id_usuario, boleto.id_rifa, boleto.id)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Boleto actualizado correctamente.")
            return rows
        except Exception as e:
            print(f"Error actualizando el boleto: {e}")
            return 0

    @staticmethod
    def delete(boleto_id):
        try:
            query = "DELETE FROM Boleto WHERE Id=%s"
            values = (boleto_id,)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("Boleto eliminado correctamente.")
            return rows
        except Exception as e:
            print(f"Error eliminando el boleto: {e}")
            return 0
