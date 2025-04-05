from pago_premio_dao import PagoPremioDAO
from models import PagoPremio


def mostrar_menu_pago_premio():
    while True:
        print("\nMenú de Gestión de Pagos de Premio")
        print("1. Mostrar todos los pagos de premio")
        print("2. Agregar un pago de premio")
        print("3. Actualizar un pago de premio")
        print("4. Eliminar un pago de premio")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            pagos = PagoPremioDAO.get_all()
            for pago in pagos:
                print(pago)

        elif opcion == "2":
            id_usuario = int(input("ID del usuario: "))
            id_rifa_apuesta = int(input("ID de la rifa/apuesta: "))
            valor_ganado = float(input("Valor ganado: "))
            nuevo_pago = PagoPremio(idusuario=id_usuario, idrifa_apuesta=id_rifa_apuesta, valorganado=valor_ganado)
            PagoPremioDAO.insert(nuevo_pago)
            print("Pago de premio agregado.")

        elif opcion == "3":
            id_pago = int(input("ID del pago a actualizar: "))
            id_usuario = int(input("Nuevo ID de usuario: "))
            id_rifa_apuesta = int(input("Nuevo ID de rifa/apuesta: "))
            valor_ganado = float(input("Nuevo valor ganado: "))
            pago_actualizado = PagoPremio(id=id_pago, idusuario=id_usuario, idrifa_apuesta=id_rifa_apuesta, valorganado=valor_ganado)
            PagoPremioDAO.update(pago_actualizado)
            print("Pago de premio actualizado.")

        elif opcion == "4":
            id_pago = int(input("ID del pago a eliminar: "))
            PagoPremioDAO.delete(id_pago)
            print("Pago de premio eliminado.")

        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_pago_premio()
