from mostrar_menu_apuesta import mostrar_menu_apuesta
from mostrar_menu_boleto import mostrar_menu_boleto
from mostrar_menu_pago_premio import mostrar_menu_pago_premio
from mostrar_menu_participacion import mostrar_menu_participacion_apuesta
from backDesarrolloWeb2.menus.mostrar_menu_rifa import mostrar_menu_rifa
from mostrar_menu_sorteo import mostrar_menu_sorteo
from mostrar_menu_transaccion import mostrar_menu_transaccion
from backDesarrolloWeb2.menus.mostrar_menu_usuario import mostrar_menu_usuario

def mostrar_menu_principal():
    while True:
        # Menú principal
        print("\n--- Menú Principal ---")
        print("1. Menú Apuesta")
        print("2. Menú Boleto")
        print("3. Menú Pago Premio")
        print("4. Menú Participación Apuesta")
        print("5. Menú Rifa")
        print("6. Menú Sorteo")
        print("7. Menú Transacción")
        print("8. Menú Usuario")
        print("9. Salir")

        # Solicitar al usuario que elija una opción
        try:
            opcion = int(input("Selecciona una opción (1-9): "))
            if opcion == 1:
                mostrar_menu_apuesta()
            elif opcion == 2:
                mostrar_menu_boleto()
            elif opcion == 3:
                mostrar_menu_pago_premio()
            elif opcion == 4:
                mostrar_menu_participacion_apuesta()
            elif opcion == 5:
                mostrar_menu_rifa()
            elif opcion == 6:
                mostrar_menu_sorteo()
            elif opcion == 7:
                mostrar_menu_transaccion()
            elif opcion == 8:
                mostrar_menu_usuario()
            elif opcion == 9:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elige un número entre 1 y 9.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    mostrar_menu_principal()