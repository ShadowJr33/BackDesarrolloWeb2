from backDesarrolloWeb2.connection import SessionLocal
from models import PagoPremio

class PagoPremioDAO:
    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                pagos = session.query(PagoPremio).all()
                return pagos
        except Exception as e:
            print(f"Error obteniendo los pagos de premio: {e}")
            return []

    @staticmethod
    def insert(pago):
        try:
            with SessionLocal() as session:
                session.add(pago)
                session.commit()
                print("Pago de premio agregado correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando pago de premio: {e}")
            return 0

    @staticmethod
    def update(pago):
        try:
            with SessionLocal() as session:
                pago_existente = session.query(PagoPremio).filter_by(id=pago.id).first()
                if pago_existente:
                    pago_existente.id_usuario = pago.id_usuario
                    pago_existente.id_rifa_apuesta = pago.id_rifa_apuesta
                    pago_existente.valor_ganado = pago.valor_ganado
                    session.commit()
                    print("Pago de premio actualizado correctamente.")
                    return 1
                else:
                    print("Pago de premio no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error actualizando pago de premio: {e}")
            return 0

    @staticmethod
    def delete(pago_id):
        try:
            with SessionLocal() as session:
                pago = session.query(PagoPremio).filter_by(id=pago_id).first()
                if pago:
                    session.delete(pago)
                    session.commit()
                    print("Pago de premio eliminado correctamente.")
                    return 1
                else:
                    print("Pago de premio no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error eliminando pago de premio: {e}")
            return 0