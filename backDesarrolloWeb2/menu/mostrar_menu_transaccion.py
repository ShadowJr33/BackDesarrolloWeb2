from backDesarrolloWeb2.routes.transaccion_routes import TransaccionDAO
from models import Transaccion
from datetime import datetime
import pytz  # Importa pytz para manejar zonas horarias

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
            id_usuario = input("ID del usuario: ")
            tipo = input("Tipo de transacción (entrada/salida): ")
            monto = float(input("Monto: "))
            
            # Obtén la fecha y hora actuales en la zona horaria de Colombia
            zona_horaria_colombia = pytz.timezone("America/Bogota")
            fecha = datetime.now(zona_horaria_colombia)

            nueva_transaccion = Transaccion(id_usuario=id_usuario, tipo=tipo, monto=monto, fecha=fecha)
            TransaccionDAO.insert(nueva_transaccion)
            print("🎉 ¡Transacción agregada exitosamente!")

        elif opcion == "3":
            id_transaccion = input("ID de la transacción a actualizar: ")
            id_usuario = input("Nuevo ID del usuario: ")
            tipo = input("Nuevo tipo de transacción (entrada/salida): ")
            monto = float(input("Nuevo monto: "))
            
            # Obtén la fecha y hora actuales en la zona horaria de Colombia
            zona_horaria_colombia = pytz.timezone("America/Bogota")
            fecha = datetime.now(zona_horaria_colombia)

            transaccion_actualizada = Transaccion(id=id_transaccion, id_usuario=id_usuario, tipo=tipo, monto=monto, fecha=fecha)
            TransaccionDAO.update(transaccion_actualizada)
            print("✅ Transacción actualizada exitosamente.")

        elif opcion == "4":
            id_transaccion = input("ID de la transacción a eliminar: ")
            TransaccionDAO.delete(id_transaccion)
            print("❌ Transacción eliminada exitosamente.")

        elif opcion == "5":
            print("👋 Saliendo del sistema de transacciones...")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_transaccion()