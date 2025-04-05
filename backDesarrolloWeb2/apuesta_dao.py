from base_dao import BaseDAO
from models import Apuesta

class ApuestaDAO(BaseDAO):
    @staticmethod
    def get_all():
        """ Obtiene todas las apuestas de la base de datos """
        try:
            query = "SELECT * FROM apuesta"
            results = BaseDAO.execute_query(query, fetch=True)

            return [Apuesta(**{
                'id': row['Id'],  # Usa 'Id' si MySQL lo devuelve con mayúscula
                'deporte': row['Deporte'],
                'campeonato': row['Campeonato'],
                'fecha_partido': row['FechaPartido'],
                'marcador': row['Marcador'],
                'valor_minimo_apuesta': row['ValorMinimoApuesta'],
                'valor_maximo_apuesta': row['ValorMaximoApuesta']
            }) for row in results] if results else []

        except Exception as e:
            print(f"Error obteniendo las apuestas: {e}")
            return []

    @staticmethod
    def insert(apuesta):
        try:
            query = "INSERT INTO apuesta (Deporte, Campeonato, FechaPartido, Marcador, ValorMinimoApuesta, ValorMaximoApuesta) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (apuesta.deporte, apuesta.campeonato, apuesta.fecha_partido, apuesta.marcador, apuesta.valor_minimo_apuesta, apuesta.valor_maximo_apuesta)
            return BaseDAO.execute_query(query, values)
        except Exception as e:
            print(f"Error insertando apuesta: {e}")
            return 0

    @staticmethod
    def update(apuesta):
        try:
            query = "UPDATE apuesta SET Deporte=%s, Campeonato=%s, FechaPartido=%s, Marcador=%s, ValorMinimoApuesta=%s, ValorMaximoApuesta=%s WHERE id=%s"
            values = (apuesta.deporte, apuesta.campeonato, apuesta.fecha_partido, apuesta.marcador, apuesta.valor_minimo_apuesta, apuesta.valor_maximo_apuesta, apuesta.id)
            return BaseDAO.execute_query(query, values)
        except Exception as e:
            print(f"Error actualizando apuesta: {e}")
            return 0

    @staticmethod
    def delete(apuesta_id):
        try:
            query = "DELETE FROM apuesta WHERE id=%s"
            return BaseDAO.execute_query(query, (apuesta_id,))
        except Exception as e:
            print(f"Error eliminando apuesta: {e}")
            return 0