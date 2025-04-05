from boleto_dao import BoletoDAO
from models import Boleto

def mostrar_menu_boleto():
    while True:
        print("\nMenú de Gestión de Boletos")
        print("1. Mostrar todos los boletos")
        print("2. Agregar un boleto")
        print("3. Actualizar un boleto")
        print("4. Eliminar un boleto")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            boletos = BoletoDAO.get_all()
            for boleto in boletos:
                print(boleto)

        elif opcion == "2":
            id_rifa = input("ID de la rifa: ")
            id_usuario = input("ID del usuario: ")
            numero_asignado = input("Número asignado: ")
            
            nuevo_boleto = Boleto(id_rifa=id_rifa, id_usuario=id_usuario, numero_asignado=numero_asignado)
            BoletoDAO.insert(nuevo_boleto)
            print("🎉 Boleto agregado exitosamente.")

        elif opcion == "3":
            id_boleto = input("ID del boleto a actualizar: ")
            id_rifa = input("Nuevo ID de la rifa: ")
            id_usuario = input("Nuevo ID del usuario: ")
            numero_asignado = input("Nuevo número asignado: ")
            
            boleto_actualizado = Boleto(id=id_boleto, id_rifa=id_rifa, id_usuario=id_usuario, numero_asignado=numero_asignado)
            BoletoDAO.update(boleto_actualizado)
            print("✅ Boleto actualizado exitosamente.")

        elif opcion == "4":
            id_boleto = input("ID del boleto a eliminar: ")
            BoletoDAO.delete(id_boleto)
            print("❌ Boleto eliminado exitosamente.")

        elif opcion == "5":
            print("👋 Saliendo del sistema de boletos...")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_boleto()