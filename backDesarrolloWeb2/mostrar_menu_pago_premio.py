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
            id_usuario = input("ID del usuario: ")
            id_rifa_apuesta = input("ID de la rifa/apuesta: ")
            valor_ganado = float(input("Valor ganado: "))

            nuevo_pago = PagoPremio(id_usuario=id_usuario, id_rifa_apuesta=id_rifa_apuesta, valor_ganado=valor_ganado)
            PagoPremioDAO.insert(nuevo_pago)
            print("🎉 ¡Pago de premio agregado exitosamente!")

        elif opcion == "3":
            id_pago = input("ID del pago de premio a actualizar: ")
            id_usuario = input("Nuevo ID del usuario: ")
            id_rifa_apuesta = input("Nuevo ID de la rifa/apuesta: ")
            valor_ganado = float(input("Nuevo valor ganado: "))

            pago_actualizado = PagoPremio(id=id_pago, id_usuario=id_usuario, id_rifa_apuesta=id_rifa_apuesta, valor_ganado=valor_ganado)
            PagoPremioDAO.update(pago_actualizado)
            print("✅ Pago de premio actualizado exitosamente.")

        elif opcion == "4":
            id_pago = input("ID del pago de premio a eliminar: ")
            PagoPremioDAO.delete(id_pago)
            print("❌ Pago de premio eliminado exitosamente.")

        elif opcion == "5":
            print("👋 Saliendo del sistema de pagos de premio...")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_pago_premio()