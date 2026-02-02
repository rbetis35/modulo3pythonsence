from contacto import Contacto
from gestor import GestorContactos

def test_funcionalidad():
    print("🧪 Iniciando pruebas unitarias...")
    gestor = GestorContactos()
    
    # Prueba 1: Agregar
    c1 = Contacto("Juan Perez", "912345678", "juan@mail.com", "Calle 123")
    gestor.agregar_contacto(c1)
    assert len(gestor.contactos) == 1
    print("✅ Prueba Agregar: PASADA")

    # Prueba 2: Buscar
    resultados = gestor.buscar_contacto("Juan")
    assert len(resultados) > 0
    print("✅ Prueba Buscar: PASADA")

    # Prueba 3: Eliminar
    gestor.eliminar_contacto("Juan Perez")
    assert len(gestor.contactos) == 0
    print("✅ Prueba Eliminar: PASADA")

    print("\n🎉 Todas las pruebas se completaron con éxito.")

if __name__ == "__main__":
    test_funcionalidad()