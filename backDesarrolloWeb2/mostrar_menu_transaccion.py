from transaccion_dao import TransaccionDAO
from models import Transaccion

def mostrar_menu_transaccion():
    while True:
        print("\nMenú de Gestión de Transacciones")
        print("1. Mostrar todas las transacciones")
        print("2. Agregar una transacción")
        print("3. Actualizar una transacción")
        print("4. Eliminar una transacción")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            transacciones = TransaccionDAO.get_all()
            for transaccion in transacciones:
                print(transaccion)

        elif opcion == "2":
            id_usuario = int(input("ID del usuario: "))
            tipo = input("Tipo de transacción ('entrada' o 'salida'): ").lower()
            monto = float(input("Monto: "))
            # No pedimos la fecha ya que se asignará automáticamente
            nueva_transaccion = Transaccion(idusuario=id_usuario, tipo=tipo, monto=monto)
            TransaccionDAO.insert(nueva_transaccion)
            print("Transacción agregada.")

        elif opcion == "3":
            id_transaccion = int(input("ID de la transacción a actualizar: "))
            id_usuario = int(input("Nuevo ID de usuario: "))
            tipo = input("Nuevo tipo de transacción ('entrada' o 'salida'): ").lower()
            monto = float(input("Nuevo monto: "))
            # No pedimos la fecha ya que se asignará automáticamente
            transaccion_actualizada = Transaccion(id=id_transaccion, idusuario=id_usuario, tipo=tipo, monto=monto)
            TransaccionDAO.update(transaccion_actualizada)
            print("Transacción actualizada.")

        elif opcion == "4":
            id_transaccion = int(input("ID de la transacción a eliminar: "))
            TransaccionDAO.delete(id_transaccion)
            print("Transacción eliminada.")

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_transaccion()
