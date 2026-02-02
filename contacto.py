class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        # El método __init__ es el "constructor". 
        # Se ejecuta automáticamente cuando creamos un nuevo contacto.
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        # Este método sirve para que, al hacer un 'print' del contacto,
        # se vea bonito y no como un código extraño.
        return f"Nombre: {self.nombre} | Tel: {self.telefono} | Email: {self.correo} | Dir: {self.direccion}"

    def actualizar_datos(self, nombre=None, telefono=None, correo=None, direccion=None):
        # Este método nos ayudará con el requerimiento de "Editar"
        if nombre: self.nombre = nombre
        if telefono: self.telefono = telefono
        if correo: self.correo = correo
        if direccion: self.direccion = direccion