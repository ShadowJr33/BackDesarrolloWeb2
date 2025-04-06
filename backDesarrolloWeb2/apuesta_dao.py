from conection import SessionLocal
from models import Apuesta

class ApuestaDAO:
    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                apuestas = session.query(Apuesta).all()
                return apuestas
        except Exception as e:
            print(f"Error obteniendo las apuestas: {e}")
            return []

    @staticmethod
    def insert(apuesta):
        try:
            with SessionLocal() as session:
                session.add(apuesta)
                session.commit()
                print("Apuesta agregada correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando usuario: {e}")
            return 0

    @staticmethod
    def update(apuesta):
        try:
            with SessionLocal() as session:
                apuesta_existente = session.query(Apuesta).filter_by(id=apuesta.id).first()
                if apuesta_existente:
                    apuesta_existente.deporte = apuesta.deporte
                    apuesta_existente.campeonato = apuesta.campeonato
                    apuesta_existente.fecha_partido = apuesta.fecha_partido
                    apuesta_existente.marcador = apuesta.marcador
                    apuesta_existente.valor_maximo_apuesta = apuesta.valor_maximo_apuesta
                    apuesta_existente.valor_maximo_apuesta = apuesta.valor_maximo_apuesta
                    session.commit()
                    print("Apuesta actualizada correctamente.")
                    return 1
                else:
                    print("Apuesta no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error actualizando apuesta: {e}")
            return 0

    @staticmethod
    def delete(apuesta_id):
        try:
            with SessionLocal() as session:
                apuesta = session.query(Apuesta).filter_by(id=apuesta_id).first()
                if apuesta:
                    session.delete(apuesta)
                    session.commit()
                    print("Apuesta eliminada correctamente.")
                    return 1
                else:
                    print("Apuesta no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error eliminando apuesta: {e}")
            return 0
