from conection import SessionLocal
from models import Usuario

class UsuarioDAO:

    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                usuarios = session.query(Usuario).all()
                return usuarios
        except Exception as e:
            print(f"Error obteniendo los usuarios: {e}")
            return []

    @staticmethod
    def insert(usuario):
        try:
            with SessionLocal() as session:
                session.add(usuario)
                session.commit()
                print("Usuario agregado correctamente.")
                return 1
        except Exception as e:
            print(f"Error insertando usuario: {e}")
            return 0

    @staticmethod
    def update(usuario):
        try:
            with SessionLocal() as session:
                usuario_existente = session.query(Usuario).filter_by(id=usuario.id).first()
                if usuario_existente:
                    usuario_existente.nombre = usuario.nombre
                    usuario_existente.correo = usuario.correo
                    usuario_existente.contraseña = usuario.contraseña
                    usuario_existente.saldo = usuario.saldo
                    session.commit()
                    print("Usuario actualizado correctamente.")
                    return 1
                else:
                    print("Usuario no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error actualizando usuario: {e}")
            return 0

    @staticmethod
    def delete(user_id):
        try:
            with SessionLocal() as session:
                usuario = session.query(Usuario).filter_by(id=user_id).first()
                if usuario:
                    session.delete(usuario)
                    session.commit()
                    print("Usuario eliminado correctamente.")
                    return 1
                else:
                    print("Usuario no encontrado.")
                    return 0
        except Exception as e:
            print(f"Error eliminando usuario: {e}")
            return 0
