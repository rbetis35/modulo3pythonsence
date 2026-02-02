class GestorContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)
        print(f"✅ Contacto '{contacto.nombre}' agregado con éxito.")

    def buscar_contacto(self, criterio):
        # 'criterio' puede ser el nombre o el teléfono
        resultados = []
        for c in self.contactos:
            # Buscamos si el criterio coincide con nombre o teléfono
            if criterio.lower() in c.nombre.lower() or criterio in c.telefono:
                resultados.append(c)
        return resultados

    def eliminar_contacto(self, nombre):
        # Buscamos el contacto por nombre exacto para eliminarlo
        for c in self.contactos:
            if c.nombre.lower() == nombre.lower():
                self.contactos.remove(c)
                print(f"🗑️ Contacto '{nombre}' eliminado.")
                return True
        print("❌ No se encontró el contacto para eliminar.")
        return False

    def mostrar_todos(self):
        if not self.contactos:
            print("📭 La agenda está vacía.")
        else:
            print("\n--- Lista de Contactos ---")
            for i, contacto in enumerate(self.contactos):
                print(f"{i+1}. {contacto}")

    def editar_contacto(self, nombre_buscar):
        for c in self.contactos:
            if c.nombre.lower() == nombre_buscar.lower():
                print(f"\n--- Editando a: {c.nombre} ---")
                print("(Deje en blanco para mantener el valor actual)")
                
                nuevo_nombre = input(f"Nuevo nombre [{c.nombre}]: ") or c.nombre
                nuevo_tel = input(f"Nuevo teléfono [{c.telefono}]: ") or c.telefono
                nuevo_email = input(f"Nuevo correo [{c.correo}]: ") or c.correo
                nueva_dir = input(f"Nueva dirección [{c.direccion}]: ") or c.direccion
                
                c.actualizar_datos(nuevo_nombre, nuevo_tel, nuevo_email, nueva_dir)
                print("✅ Contacto actualizado correctamente.")
                return True
        
        print("❌ No se encontró el contacto para editar.")
        return False 