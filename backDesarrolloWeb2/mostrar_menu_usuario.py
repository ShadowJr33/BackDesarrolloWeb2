from usuario_dao import UsuarioDAO
from models import Usuario

def mostrar_menu_usuario():
    while True:
        print("\n🔹 Menú de Gestión de Usuarios 🔹")
        print("1. Mostrar todos los usuarios")
        print("2. Agregar un usuario")
        print("3. Actualizar un usuario")
        print("4. Eliminar un usuario")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            usuarios = UsuarioDAO.get_all()
            if usuarios:
                for usuario in usuarios:
                    print(usuario)
            else:
                print("No hay usuarios registrados.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contraseña = input("Contraseña: ")
            try:
                saldo = float(input("Saldo inicial: "))
            except ValueError:
                print("Saldo inválido.")
                continue

            nuevo_usuario = Usuario(nombre=nombre, correo=correo, contraseña=contraseña, saldo=saldo)
            UsuarioDAO.insert(nuevo_usuario)

        elif opcion == "3":
            try:
                id_usuario = int(input("ID del usuario a actualizar: "))
                nombre = input("Nuevo nombre: ")
                correo = input("Nuevo correo: ")
                contraseña = input("Nueva contraseña: ")
                saldo = float(input("Nuevo saldo: "))

                usuario_actualizado = Usuario(id=id_usuario, nombre=nombre, correo=correo, contraseña=contraseña, saldo=saldo)
                UsuarioDAO.update(usuario_actualizado)
            except ValueError:
                print("ID o saldo inválido.")
                continue

        elif opcion == "4":
            try:
                id_usuario = int(input("ID del usuario a eliminar: "))
                UsuarioDAO.delete(id_usuario)
            except ValueError:
                print("ID inválido.")
                continue

        elif opcion == "5":
            print("👋 Saliendo del menú...")
            break
        else:
            print("❌ Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    mostrar_menu_usuario()
