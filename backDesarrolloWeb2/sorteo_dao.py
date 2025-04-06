from conection import SessionLocal
from models import Sorteo

class SorteoDAO:
    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                sorteos = session.query(Sorteo).all()
                return sorteos
        except Exception as e:
            print(f"Error obteniendo los sorteos: {e}")
            return []

    @staticmethod
    def insert(sorteo):
        try:
            with SessionLocal() as session:
                session.add(sorteo)
                session.commit()
                print("Sorteo agregado correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando sorteo: {e}")
            return 0

    @staticmethod
    def update(sorteo):
        try:
            with SessionLocal() as session:
                sorteo_existente = session.query(Sorteo).filter_by(id=sorteo.id).first()
                if sorteo_existente:
                    sorteo_existente.id_rifa = sorteo.id_rifa
                    sorteo_existente.numero_ganador = sorteo.numero_ganador
                    session.commit()
                    print("Sorteo actualizado correctamente.")
                    return 1
                else:
                    print("Sorteo no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error actualizando sorteo: {e}")
            return 0

    @staticmethod
    def delete(sorteo_id):
        try:
            with SessionLocal() as session:
                sorteo = session.query(Sorteo).filter_by(id=sorteo_id).first()
                if sorteo:
                    session.delete(sorteo)
                    session.commit()
                    print("Sorteo eliminado correctamente.")
                    return 1
                else:
                    print("Sorteo no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error eliminando sorteo: {e}")
            return 0
