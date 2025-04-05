from backDesarrolloWeb2.llamadosDaos.rifa_dao import RifaDAO
from backDesarrolloWeb2.models import Rifa
from datetime import datetime

def mostrar_menu_rifa():
    while True:
        print("\nMenú de Gestión de Rifas")
        print("1. Mostrar todas las rifas")
        print("2. Agregar una rifa")
        print("3. Actualizar una rifa")
        print("4. Eliminar una rifa")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            rifas = RifaDAO.get_all()
            for rifa in rifas:
                print(rifa)

        elif opcion == "2":
            nombre = input("Nombre de la rifa: ")
            numero_maximo_participantes = int(input("Número máximo de participantes: "))
            valor = float(input("Valor: "))

            # Manejo de fechas con validación
            while True:
                try:
                    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
                    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()

                    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
                    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()

                    if fecha_inicio > fecha_fin:
                        print("⚠️ La fecha de inicio no puede ser mayor que la fecha de fin. Intente nuevamente.")
                        continue
                    break
                except ValueError:
                    print("⚠️ Formato incorrecto. Use el formato YYYY-MM-DD.")

            premio_principal = input("Premio principal: ")
            premios_secundarios = input("Premios secundarios (separados por coma, opcional): ")

            nueva_rifa = Rifa(nombre=nombre, numero_maximo_participantes=numero_maximo_participantes,
                              valor=valor, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin,
                              premio_principal=premio_principal, premios_secundarios=premios_secundarios)

            RifaDAO.insert(nueva_rifa)
            print("🎉 ¡Rifa agregada exitosamente!")

        elif opcion == "3":
            id_rifa = input("ID de la rifa a actualizar: ")
            nombre = input("Nuevo nombre: ")
            numero_maximo_participantes = int(input("Nuevo número máximo de participantes: "))
            valor = float(input("Nuevo valor: "))

            # Validación de fechas
            while True:
                try:
                    fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
                    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d").date()

                    fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
                    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d").date()

                    if fecha_inicio > fecha_fin:
                        print("⚠️ La fecha de inicio no puede ser mayor que la fecha de fin. Intente nuevamente.")
                        continue
                    break
                except ValueError:
                    print("⚠️ Formato incorrecto. Use el formato YYYY-MM-DD.")

            premio_principal = input("Nuevo premio principal: ")
            premios_secundarios = input("Nuevos premios secundarios (separados por coma, opcional): ")

            rifa_actualizada = Rifa(id=id_rifa, nombre=nombre, numero_maximo_participantes=numero_maximo_participantes,
                                    valor=valor, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin,
                                    premio_principal=premio_principal, premios_secundarios=premios_secundarios)

            RifaDAO.update(rifa_actualizada)
            print("✅ Rifa actualizada exitosamente.")

        elif opcion == "4":
            id_rifa = input("ID de la rifa a eliminar: ")
            RifaDAO.delete(id_rifa)
            print("❌ Rifa eliminada exitosamente.")

        elif opcion == "5":
            print("👋 Saliendo del sistema de rifas...")
            break
        else:
            print("⚠️ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_rifa()
