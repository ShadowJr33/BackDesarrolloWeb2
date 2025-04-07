from conection import SessionLocal
from models import Transaccion

class TransaccionDAO:
    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                transacciones = session.query(Transaccion).all()
                return transacciones
        except Exception as e:
            print(f"Error obteniendo las transacciones: {e}")
            return []

    @staticmethod
    def insert(transaccion):
        try:
            with SessionLocal() as session:
                session.add(transaccion)
                session.commit()
                print("Transacción agregada correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando transacción: {e}")
            return 0

    @staticmethod
    def update(transaccion):
        try:
            with SessionLocal() as session:
                transaccion_existente = session.query(Transaccion).filter_by(id=transaccion.id).first()
                if transaccion_existente:
                    transaccion_existente.id_usuario = transaccion.id_usuario
                    transaccion_existente.tipo = transaccion.tipo
                    transaccion_existente.monto = transaccion.monto
                    transaccion_existente.fecha = transaccion.fecha
                    session.commit()
                    print("Transacción actualizada correctamente.")
                    return 1
                else:
                    print("Transacción no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error actualizando transacción: {e}")
            return 0

    @staticmethod
    def delete(transaccion_id):
        try:
            with SessionLocal() as session:
                transaccion = session.query(Transaccion).filter_by(id=transaccion_id).first()
                if transaccion:
                    session.delete(transaccion)
                    session.commit()
                    print("Transacción eliminada correctamente.")
                    return 1
                else:
                    print("Transacción no encontrada.")
                    return 0
        except Exception as e:
            print(f"Error eliminando transacción: {e}")
            return 0