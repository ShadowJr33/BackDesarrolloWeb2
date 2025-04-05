from backDesarrolloWeb2.conection import SessionLocal
from backDesarrolloWeb2.models import Rifa

class RifaDAO:
    
    @staticmethod
    def get_all():
        """Obtiene todas las rifas."""
        try:
            with SessionLocal() as session:
                return session.query(Rifa).all()
        except Exception as e:
            print(f"Error obteniendo rifas: {e}")
            return []

    @staticmethod
    def insert(rifa):
        """Inserta una nueva rifa."""
        try:
            with SessionLocal() as session:
                session.add(rifa)
                session.commit()
                print("Rifa agregada correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando rifa: {e}")
            return 0

    @staticmethod
    def update(rifa):
        """Actualiza una rifa existente."""
        try:
            with SessionLocal() as session:
                rifa_db = session.query(Rifa).filter_by(id=rifa.id).first()
                if rifa_db:
                    rifa_db.nombre = rifa.nombre
                    rifa_db.numero_maximo_participantes = rifa.numero_maximo_participantes
                    rifa_db.valor = rifa.valor
                    rifa_db.fecha_inicio = rifa.fecha_inicio
                    rifa_db.fecha_fin = rifa.fecha_fin
                    rifa_db.premio_principal = rifa.premio_principal
                    rifa_db.premios_secundarios = rifa.premios_secundarios
                    session.commit()
                    print("Rifa actualizada correctamente.")
                    return 1
                else:
                    print("Rifa no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error actualizando rifa: {e}")
            return 0

    @staticmethod
    def delete(rifa_id):
        """Elimina una rifa por ID."""
        try:
            with SessionLocal() as session:
                rifa = session.query(Rifa).filter_by(id=rifa_id).first()
                if rifa:
                    session.delete(rifa)
                    session.commit()
                    print("Rifa eliminada correctamente.")
                    return 1
                else:
                    print("Rifa no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error eliminando rifa: {e}")
            return 0
