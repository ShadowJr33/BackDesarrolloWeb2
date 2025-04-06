from conection import SessionLocal
from models import Boleto

class BoletoDAO:

    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                boletos = session.query(Boleto).all()
                return boletos
        except Exception as e:
            print(f"Error obteniendo los boletos: {e}")
            return []

    @staticmethod
    def insert(boleto):
        try:
            with SessionLocal() as session:
                session.add(boleto)
                session.commit()
                print("Boleto agregado correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando boleto: {e}")
            return 0

    @staticmethod
    def update(boleto):
        try:
            with SessionLocal() as session:
                boleto_existente = session.query(Boleto).filter_by(id=boleto.id).first()
                if boleto_existente:
                    boleto_existente.id_rifa = boleto.id_rifa
                    boleto_existente.id_usuario = boleto.id_usuario
                    boleto_existente.numero_asignado = boleto.numero_asignado
                    session.commit()
                    print("Boleto actualizado correctamente.")
                    return 1
                else:
                    print("Boleto no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error actualizando boleto: {e}")
            return 0

    @staticmethod
    def delete(boleto_id):
        try:
            with SessionLocal() as session:
                boleto = session.query(Boleto).filter_by(id=boleto_id).first()
                if boleto:
                    session.delete(boleto)
                    session.commit()
                    print("Boleto eliminado correctamente.")
                    return 1
                else:
                    print("Boleto no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error eliminando boleto: {e}")
            return 0
