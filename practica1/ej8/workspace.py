from ej8 import *

def main():
    # Crear integrantes
    luis = Integrante("Luis", "luis@correo.com")
    maria = Integrante("Maria", "maria@correo.com")
    
    # Crear un tablero con un líder
    tablero1 = Tablero("Tablero de Proyecto", luis)
    print("\n")
    
    # Crear tareas
    tarea1 = tablero1.crear_tarea("Desarrollar módulo de autenticación", "Desarrollo del módulo de login", datetime(2025, 3, 10), 3, "Programación")
    print("\n")
    tarea2 = tablero1.crear_tarea("Diseño de interfaz de login", "Diseñar la pantalla de login", datetime(2025, 3, 8), 2, "DIU")
    print("\n")
    
    # Asignar tareas
    tablero1.asignar_tarea(tarea1, luis, datetime.now())  # Luis asume tarea1
    print("\n")
    tablero1.asignar_tarea(tarea2, maria, datetime.now())  # Maria asume tarea2
    print("\n")

    # Listar tareas pendientes
    print(tablero1.listar_tareas_pendientes())
    print("\n")

if __name__ == "__main__":
    main()
