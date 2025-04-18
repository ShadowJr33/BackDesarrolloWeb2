from backDesarrolloWeb2.connection import SessionLocal
from models import ParticipacionApuesta

class ParticipacionApuestaDAO:

    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                participaciones_apuestas = session.query(ParticipacionApuesta).all()
                return participaciones_apuestas
        except Exception as e:
            print(f"Error obteniendo los participaciones de apuestas: {e}")
            return []

    @staticmethod
    def insert(participacion_apuesta):
        try:
            with SessionLocal() as session:
                session.add(participacion_apuesta)
                session.commit()
                print("ParticipacionApuesta agregado correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando participacion de apuesta: {e}")
            return 0

    @staticmethod
    def update(participacion_apuesta):
        try:
            with SessionLocal() as session:
                participacion_apuesta_existente = session.query(ParticipacionApuesta).filter_by(id=participacion_apuesta.id).first()
                if participacion_apuesta_existente:
                    participacion_apuesta_existente.id_apuesta = participacion_apuesta.id_apuesta
                    participacion_apuesta_existente.id_usuario = participacion_apuesta.id_usuario
                    participacion_apuesta_existente.valor_apostado = participacion_apuesta.valor_apostado
                    session.commit()
                    print("Participacion de apuesta actualizada correctamente.")
                    return 1
                else:
                    print("Participacion de apuesta no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error actualizando participacion de apuesta: {e}")
            return 0

    @staticmethod
    def delete(user_id):
        try:
            with SessionLocal() as session:
                participacion_apuesta = session.query(ParticipacionApuesta).filter_by(id=user_id).first()
                if participacion_apuesta:
                    session.delete(participacion_apuesta)
                    session.commit()
                    print("Participacion de apuesta eliminada correctamente.")
                    return 1
                else:
                    print("Participacion de apuesta no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error eliminanda participacion de apuesta: {e}")
            return 0
