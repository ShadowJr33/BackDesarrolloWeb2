from base_dao import BaseDAO
from models import Sorteo

class SorteoDAO(BaseDAO):

    @staticmethod
    def get_all():
        """ Obtiene todos los sorteos de la base de datos """
        try:
            query = "SELECT * FROM sorteo"
            results = BaseDAO.execute_query(query, fetch=True)

            return [Sorteo(**{
                'id': row['Id'],  # Usa 'Id' si MySQL lo devuelve con mayúscula
                'id_rifa': row['IdRifa'],
                'numero_ganador': row['NumeroGanador']
            }) for row in results] if results else []

        except Exception as e:
            print(f"Error obteniendo los sorteos: {e}")
            return []

    @staticmethod
    def insert(sorteo):
        """ Inserta un nuevo sorteo en la base de datos """
        try:
            query = "INSERT INTO sorteo (IdRifa, NumeroGanador) VALUES (%s, %s)"
            values = (sorteo.id_rifa, sorteo.numero_ganador)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("🎉 Sorteo agregado exitosamente.")
            return rows
        except Exception as e:
            print(f"Error insertando el sorteo: {e}")
            return 0

    @staticmethod
    def update(sorteo):
        """ Actualiza un sorteo existente en la base de datos """
        try:
            query = "UPDATE sorteo SET IdRifa=%s, NumeroGanador=%s WHERE Id=%s"
            values = (sorteo.id_rifa, sorteo.numero_ganador, sorteo.id)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("🔄 Sorteo actualizado exitosamente.")
            return rows
        except Exception as e:
            print(f"Error actualizando el sorteo: {e}")
            return 0

    @staticmethod
    def delete(sorteo_id):
        """ Elimina un sorteo de la base de datos por su ID """
        try:
            query = "DELETE FROM sorteo WHERE Id=%s"
            values = (sorteo_id,)
            rows = BaseDAO.execute_query(query, values)
            if rows > 0:
                print("❌ Sorteo eliminado exitosamente.")
            return rows
        except Exception as e:
            print(f"Error eliminando el sorteo: {e}")
            return 0
