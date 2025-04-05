from base_dao import BaseDAO
from models import ParticipacionApuesta

class ParticipacionApuestaDAO(BaseDAO):
    
    @staticmethod
    def get_all():
        """ Obtiene todas las participaciones en apuestas de la base de datos """
        try:
            query = "SELECT * FROM participacionapuesta"
            results = BaseDAO.execute_query(query, fetch=True)
            
            return [ParticipacionApuesta(**{
                'id': row['Id'],
                'id_apuesta': row['IdApuesta'],
                'id_usuario': row['IdUsuario'],
                'valor_apostado': row['ValorApostado']
            }) for row in results] if results else []
        
        except Exception as e:
            print(f"Error obteniendo las participaciones en apuestas: {e}")
            return []
    
    @staticmethod
    def insert(participacion):
        """ Inserta una nueva participación en una apuesta """
        try:
            query = """
                INSERT INTO participacionapuesta (IdApuesta, IdUsuario, ValorApostado) 
                VALUES (%s, %s, %s)
            """
            values = (participacion.id_apuesta, participacion.id_usuario, participacion.valor_apostado)
            rows = BaseDAO.execute_query(query, values)
            
            if rows > 0:
                print("Participación en apuesta agregada correctamente.")
            return rows
        
        except Exception as e:
            print(f"Error insertando la participación en la apuesta: {e}")
            return 0
    
    @staticmethod
    def update(participacion):
        """ Actualiza una participación en una apuesta existente """
        try:
            query = """
                UPDATE participacionapuesta 
                SET IdApuesta=%s, IdUsuario=%s, ValorApostado=%s 
                WHERE Id=%s
            """
            values = (participacion.id_apuesta, participacion.id_usuario, participacion.valor_apostado, participacion.id)
            rows = BaseDAO.execute_query(query, values)
            
            if rows > 0:
                print("Participación en apuesta actualizada correctamente.")
            return rows
        
        except Exception as e:
            print(f"Error actualizando la participación en la apuesta: {e}")
            return 0
    
    @staticmethod
    def delete(participacion_id):
        """ Elimina una participación en una apuesta por su ID """
        try:
            query = "DELETE FROM participacionapuesta WHERE Id=%s"
            values = (participacion_id,)
            rows = BaseDAO.execute_query(query, values)
            
            if rows > 0:
                print("Participación en apuesta eliminada correctamente.")
            return rows
        
        except Exception as e:
            print(f"Error eliminando la participación en la apuesta: {e}")
            return 0
