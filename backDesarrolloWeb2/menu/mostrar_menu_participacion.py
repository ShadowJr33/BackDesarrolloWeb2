from backDesarrolloWeb2.routes.participacion_apuesta_dao import ParticipacionApuestaDAO
from models import ParticipacionApuesta

def mostrar_menu_participacion_apuesta():
    while True:
        print("\nMenú de Gestión de Participaciones en Apuestas")
        print("1. Mostrar todas las participaciones")
        print("2. Agregar una participación")
        print("3. Actualizar una participación")
        print("4. Eliminar una participación")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            participaciones = ParticipacionApuestaDAO.get_all()
            for participacion in participaciones:
                print(participacion)

        elif opcion == "2":
            id_apuesta = input("ID de la apuesta: ")
            id_usuario = input("ID del usuario: ")
            valor_apostado = float(input("Valor apostado: "))
            
            nueva_participacion = ParticipacionApuesta(id_apuesta=id_apuesta, id_usuario=id_usuario, valor_apostado=valor_apostado)
            ParticipacionApuestaDAO.insert(nueva_participacion)
            print("🎉 Participación agregada exitosamente.")

        elif opcion == "3":
            id_participacion = input("ID de la participación a actualizar: ")
            id_apuesta = input("Nuevo ID de la apuesta: ")
            id_usuario = input("Nuevo ID del usuario: ")
            valor_apostado = float(input("Nuevo valor apostado: "))
            
            participacion_actualizada = ParticipacionApuesta(id=id_participacion, id_apuesta=id_apuesta, id_usuario=id_usuario, valor_apostado=valor_apostado)
            ParticipacionApuestaDAO.update(participacion_actualizada)
            print("✏️ Participación actualizada exitosamente.")

        elif opcion == "4":
            id_participacion = input("ID de la participación a eliminar: ")
            ParticipacionApuestaDAO.delete(id_participacion)
            print("❌ Participación eliminada exitosamente.")

        elif opcion == "5":
            print("👋 Saliendo del sistema de participaciones...")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_participacion_apuesta()
