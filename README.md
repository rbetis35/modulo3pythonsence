README — Sistema de Gestión de Contactos
====================================================

1) Objetivo
-----------
Desarrollar una aplicación de consola en Python para organizar y administrar información personal de clientes.
El sistema permite:
- Registrar nuevos contactos (Nombre, Teléfono, Correo, Dirección).
- Listar todos los contactos guardados.
- Buscar contactos (por coincidencia en nombre o número de teléfono).
- Editar la información de contactos existentes.
- Eliminar contactos del registro.
- Salir del sistema de forma segura.

2) Requisitos
-------------
- Python 3.x
- No se requieren librerías externas (Standard Library únicamente).

3) Cómo ejecutar
----------------
- Abre la terminal (CMD o PowerShell en Windows, Terminal en macOS/Linux).
- Dirígete a la carpeta del proyecto usando el comando `cd`:
   (Ejemplo: cd Documentos\Proyecto_SENCE)

- Ejecuta el archivo principal:
   python main.py

- Si el comando anterior no funciona (por ejemplo, aparece un error indicando que no se reconoce `python`),
  en Windows también puedes ejecutar usando el lanzador de Python:

   py main.py

4) Cómo ejecutar las pruebas
-----------------------------
El proyecto incluye un archivo de pruebas (`test_sistema.py`) que valida las funcionalidades principales del sistema (agregar, buscar y eliminar contactos).

Para ejecutar las pruebas:

   python test_sistema.py

- Si el comando anterior no funciona, usa:

   py test_sistema.py

Si todas las pruebas pasan correctamente, verás el mensaje:
   🎉 Todas las pruebas se completaron con éxito.

5) Estructura y Lógica (POO)
----------------------------
A diferencia de un sistema básico de diccionarios, este proyecto utiliza **Programación Orientada a Objetos (POO)** para una mejor escalabilidad:

- **Clase Contacto**: Define el objeto contacto con sus atributos (nombre, teléfono, correo, dirección) y métodos de actualización.
- **Clase GestorContactos**: Actúa como el controlador del sistema, gestionando una **lista** de objetos de tipo Contacto.
- **Encapsulación**: Se gestionan los datos a través de métodos internos de las clases.

6) Menú del sistema
-------------------
1) Agregar contacto
2) Mostrar todos los contactos
3) Buscar contacto
4) Editar contacto
5) Eliminar contacto
6) Salir

7) Validaciones y Características
---------------------------------
- **Búsqueda Flexible**: Permite encontrar contactos aunque solo se escriba una parte del nombre o del número.
- **Edición Inteligente**: Al editar, si se deja un campo en blanco, el sistema conserva el dato original.
- **Control de Vacíos**: Si la agenda no tiene registros, el sistema informa al usuario en lugar de mostrar errores.
- **Modularidad**: El código está separado en archivos (`contacto.py`, `gestor.py`, `main.py`) para facilitar su mantenimiento.
