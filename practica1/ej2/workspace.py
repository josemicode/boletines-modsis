from datetime import datetime
from ej2 import *

def main():
    # Crear instancias de cursos (grabados y en vivo)
    curso1 = CursoGrabado("Python Básico", "Introducción a Python", 50)
    curso2 = CursoGrabado("Java Avanzado", "Programación avanzada en Java", 70)
    curso3 = CursoEnVivo("Machine Learning", "Curso intensivo de ML", 120, "2025-05-10", 15, 10, 5)
    curso4 = CursoEnVivo("Redes y Seguridad", "Seguridad informática y redes", 150, "2025-06-20", 20, 8, 10)
    
    # Crear instancias de usuarios
    usuario1 = Usuario("Juan", "juan@example.com", "pass123")
    usuario2 = Usuario("Maria", "maria@example.com", "secure456")
    usuario3 = Usuario("David", "david@example.com", "clave789")
    
    # Inscribir usuarios en cursos
    usuario1.inscribirseEnCurso(curso1, 50) 
    usuario1.inscribirseEnCurso(curso3, 120)
    usuario2.inscribirseEnCurso(curso2, 70)
    usuario2.inscribirseEnCurso(curso4, 150)
    usuario3.inscribirseEnCurso(curso1, 50)
    usuario3.inscribirseEnCurso(curso2, 70)
    usuario3.inscribirseEnCurso(curso3, 120)
    
    # Valorar cursos
    usuario1.valorarCurso(curso1, 4, "Muy buen curso, claro y conciso.")
    usuario1.valorarCurso(curso3, 5, "Excelente contenido y profesor.")
    usuario2.valorarCurso(curso2, 3, "Esperaba más profundidad en algunos temas.")
    usuario2.valorarCurso(curso4, 4, "Buen curso, pero el material podría mejorar.")
    usuario3.valorarCurso(curso1, 5, "Me encantó la manera de explicar del profesor.")
    usuario3.valorarCurso(curso2, 4, "Contenido avanzado y bien estructurado.")
    usuario3.valorarCurso(curso3, 5, "Increíble curso, muy recomendable.")
    
    # Obtener y mostrar el top 10 de cursos mejor valorados
    cursos = [curso1, curso2, curso3, curso4]
    top_cursos = Curso.obtenerTopCursosPorValoracion(cursos, top_n=10)
    
    print("\nTop 10 cursos mejor valorados:")
    for curso in top_cursos:
        print(f"{curso.nombre} - Valoración promedio: {curso.getPromedioValoraciones():.2f}")
    
    # Mostrar historial de inscripciones
    print("\nHistorial de inscripciones de los usuarios:")
    print(f"\n{usuario1.nombre}:")
    usuario1.historial_de_inscripciones()
    
    print(f"\n{usuario2.nombre}:")
    usuario2.historial_de_inscripciones()
    
    print(f"\n{usuario3.nombre}:")
    usuario3.historial_de_inscripciones()

if __name__ == "__main__":
    main()
