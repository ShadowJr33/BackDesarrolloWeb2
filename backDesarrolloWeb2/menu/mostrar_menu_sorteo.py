from backDesarrolloWeb2.routes.sorteo_dao import SorteoDAO
from models import Sorteo

def mostrar_menu_sorteo():
    while True:
        print("\nMenú de Gestión de Sorteos")
        print("1. Mostrar todos los sorteos")
        print("2. Agregar un sorteo")
        print("3. Modificar un sorteo")
        print("4. Eliminar un sorteo")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            sorteos = SorteoDAO.get_all()
            for sorteo in sorteos:
                print(sorteo)

        elif opcion == "2":
            id_rifa = input("ID de la rifa: ")
            numero_ganador = input("Número ganador: ")
            
            nuevo_sorteo = Sorteo(id_rifa=id_rifa, numero_ganador=numero_ganador)
            SorteoDAO.insert(nuevo_sorteo)
            print("🎉 Sorteo agregado exitosamente.")

        elif opcion == "3":
            id_sorteo = input("ID del sorteo a modificar: ")
            sorteo_existente = SorteoDAO.get_all()
            
            # Verifica si el sorteo existe antes de actualizar
            if any(sorteo.id == int(id_sorteo) for sorteo in sorteo_existente):
                id_rifa = input("Nuevo ID de la rifa: ")
                numero_ganador = input("Nuevo número ganador: ")
                
                sorteo_actualizado = Sorteo(id=id_sorteo, id_rifa=id_rifa, numero_ganador=numero_ganador)
                SorteoDAO.update(sorteo_actualizado)
                print("🔄 Sorteo actualizado exitosamente.")
            else:
                print("⚠️ El ID del sorteo no existe.")

        elif opcion == "4":
            id_sorteo = input("ID del sorteo a eliminar: ")
            SorteoDAO.delete(id_sorteo)
            print("❌ Sorteo eliminado exitosamente.")

        elif opcion == "5":
            print("👋 Saliendo del sistema de sorteos...")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_sorteo()
