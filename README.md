from contacto import Contacto
from gestor import GestorContactos

def menu():
    gestor = GestorContactos()
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            correo = input("Correo: ")
            direccion = input("Dirección: ")
            nuevo = Contacto(nombre, telefono, correo, direccion)
            gestor.agregar_contacto(nuevo)

        elif opcion == "2":
            gestor.mostrar_todos()

        elif opcion == "3":
            criterio = input("Ingrese nombre o teléfono a buscar: ")
            encontrados = gestor.buscar_contacto(criterio)
            if encontrados:
                print("\n🔍 Resultados encontrados:")
                for c in encontrados:
                    print(c)
            else:
                print("⚠️ No se encontraron coincidencias.")

        elif opcion == "4":
            nombre = input("Nombre del contacto a editar: ")
            gestor.editar_contacto(nombre)

        elif opcion == "5":
            nombre = input("Nombre del contacto a eliminar: ")
            gestor.eliminar_contacto(nombre)

        elif opcion == "6":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("🚫 Opción no válida.")

if __name__ == "__main__":
    menu()
