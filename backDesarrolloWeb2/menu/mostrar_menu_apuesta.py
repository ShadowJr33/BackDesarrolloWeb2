from backDesarrolloWeb2.routes.apuesta_routes import ApuestaDAO
from models import Apuesta
from datetime import datetime

def mostrar_menu_apuesta():
    while True:
        print("\nMenú de Gestión de Apuestas")
        print("1. Mostrar todas las apuestas")
        print("2. Agregar una apuesta")
        print("3. Actualizar una apuesta")
        print("4. Eliminar una apuesta")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            apuestas = ApuestaDAO.get_all()
            for apuesta in apuestas:
                print(apuesta)

        elif opcion == "2":
            deporte = input("Deporte: ")
            campeonato = input("Campeonato: ")
            fecha_partido = input("Fecha del partido (YYYY-MM-DD): ")
            marcador = input("Marcador esperado: ")
            valor_minimo_apuesta = float(input("Valor mínimo de apuesta: "))
            valor_maximo_apuesta = float(input("Valor máximo de apuesta: "))
            
            nueva_apuesta = Apuesta(deporte=deporte, campeonato=campeonato, 
                                   fecha_partido=fecha_partido, marcador=marcador, 
                                   valor_minimo_apuesta=valor_minimo_apuesta, 
                                   valor_maximo_apuesta=valor_maximo_apuesta)
            ApuestaDAO.insert(nueva_apuesta)
            print("🎉 ¡Apuesta agregada exitosamente!")

        elif opcion == "3":
            id_apuesta = input("ID de la apuesta a actualizar: ")
            deporte = input("Nuevo deporte: ")
            campeonato = input("Nuevo campeonato: ")
            fecha_partido = input("Nueva fecha del partido (YYYY-MM-DD): ")
            marcador = input("Nuevo marcador esperado: ")
            valor_minimo_apuesta = float(input("Nuevo valor mínimo de apuesta: "))
            valor_maximo_apuesta = float(input("Nuevo valor máximo de apuesta: "))
            
            apuesta_actualizada = Apuesta(id=id_apuesta, deporte=deporte, campeonato=campeonato, 
                                         fecha_partido=fecha_partido, marcador=marcador, 
                                         valor_minimo_apuesta=valor_minimo_apuesta, 
                                         valor_maximo_apuesta=valor_maximo_apuesta)
            ApuestaDAO.update(apuesta_actualizada)
            print("✅ Apuesta actualizada exitosamente.")

        elif opcion == "4":
            id_apuesta = input("ID de la apuesta a eliminar: ")
            ApuestaDAO.delete(id_apuesta)
            print("❌ Apuesta eliminada exitosamente.")

        elif opcion == "5":
            print("👋 Saliendo del sistema de apuestas...")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_apuesta()
