from ej2 import *


def main():
    # Crear algunos cursos
    curso_grabado_1 = CursoGrabado("Curso Grabado 1", "Curso grabado sobre Python", 50)
    curso_en_vivo_1 = CursoEnVivo("Curso en Vivo 1", "Curso en vivo sobre IA", 100, "2025-03-01", 10, 5, 10)
    curso_grabado_2 = CursoGrabado("Curso Grabado 2", "Curso avanzado de Python", 60)
    curso_en_vivo_2 = CursoEnVivo("Curso en Vivo 2", "Curso en vivo sobre Data Science", 150, "2025-04-01", 20, 10, 5)

    # Crear usuarios
    usuario1 = Usuario("Juan", "juanPerez@example.com", "12123")
    usuario2 = Usuario("Maria", "mariaBez@example.com", "116911")
    
    # Inscribirse en cursos
    usuario1.inscribirseEnCurso(curso_grabado_1, 50)
    usuario1.inscribirseEnCurso(curso_en_vivo_1, 100)
    usuario2.inscribirseEnCurso(curso_grabado_2, 60)
    usuario2.inscribirseEnCurso(curso_en_vivo_2, 150)
    
    # Valorar los cursos
    usuario1.valorarCurso(curso_grabado_1, 4, "Casi perfecto pero los examenes muy liosos.")
    usuario1.valorarCurso(curso_en_vivo_1, 5, "Chapó.")
    usuario2.valorarCurso(curso_grabado_2, 3, "Mmm flojillo.")
    usuario2.valorarCurso(curso_en_vivo_2, 4, "Muy interesante, pero dificil de narices.")
    
    # Obtener el top 10 de los cursos por valoración
    cursos = [curso_grabado_1, curso_en_vivo_1, curso_grabado_2, curso_en_vivo_2]
    top_cursos = Curso.obtenerTopCursosPorValoracion(cursos, top_n=10)
    
    # Mostrar los cursos mejor valorados
    print("\nTop 10 cursos por valoración:")
    for curso in top_cursos:
        print(f"{curso.nombre} - Valoración promedio: {curso.getPromedioValoraciones():.2f}")
    
   

if __name__ == "__main__":
    main()
