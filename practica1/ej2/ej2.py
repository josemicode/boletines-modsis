from abc import ABC, abstractmethod
from datetime import datetime

class Curso(ABC):
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.valoraciones = []
        
    def agregarValoracion(self, puntaje, comentario, fecha=None):
        if 1 <= puntaje <= 5:
            self.valoraciones.append(Valoracion(puntaje, comentario, fecha))
        else:
            print("El puntaje debe estar entre 1 y 5.")
        
    def getPromedioValoraciones(self):
        if not self.valoraciones:
            return 0
        return sum(v.puntaje for v in self.valoraciones) / len(self.valoraciones)
    
    def inscribirUsuario(self, usuario, cantidad, fecha):
        pass
    
    
    @classmethod
    def obtenerPromedioInscriptos(cls, cursos):
        grabados = 0
        en_vivo = 0
        contador_grabados = 0
        contador_en_vivo = 0
        
        for curso in cursos:
            if isinstance(curso, CursoGrabado):
                grabados += len(curso.inscripciones)
                contador_grabados += 1
            elif isinstance(curso, CursoEnVivo):
                en_vivo += len(curso.inscripciones)
                contador_en_vivo += 1
        
        promedio_grabados = grabados / contador_grabados if contador_grabados else 0
        promedio_en_vivo = en_vivo / contador_en_vivo if contador_en_vivo else 0
        return promedio_grabados, promedio_en_vivo
    
    @classmethod
    def obtenerTopCursosPorValoracion(cls, cursos, top_n=10):
        # Crear una lista de tuplas (curso, promedio) y ordenarla manualmente
        cursos_promedio = []
        
        for curso in cursos:
            promedio = curso.getPromedioValoraciones()
            cursos_promedio.append((curso, promedio))
        
        # Ordenamos la lista de cursos por el promedio de mayor a menor
        cursos_promedio.sort(key=lambda x: x[1], reverse=True)
        
        # Devolvemos solo los cursos ordenados
        return [curso for curso, _ in cursos_promedio[:top_n]]
    
    
    
    
    
    
    
class CursoGrabado(Curso):
    def __init__(self, nombre, descripcion, precio):
        super().__init__(nombre, descripcion)
        self.precio = precio  

    def inscribirUsuario(self, usuario, cantidad_pagada, fecha):
        
        if cantidad_pagada < self.precio:
            print(f"{usuario.nombre} no pagó suficiente para inscribirse en '{self.nombre}'.")
            return

        usuario.cursos_inscritos.append({'curso': self, 'cantidad_pagada': cantidad_pagada})
        print(f"{usuario.nombre} se inscribió en el curso grabado '{self.nombre}' pagando €{cantidad_pagada}.")

    
    
    
    
    
    
class CursoEnVivo(Curso):
    def __init__(self, nombre, descripcion, precio, fecha_inicio, cupo_maximo, inscripciones_minimas, bono_porcentaje):
        super().__init__(nombre, descripcion)
        self.precio = precio
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        self.cupo_maximo = cupo_maximo
        self.inscripciones = []  # Lista de usuarios inscritos
        self.inscripciones_minimas = inscripciones_minimas
        self.bono_porcentaje = bono_porcentaje
        self.cupos_disponibles = cupo_maximo

    def inscribirUsuario(self, usuario, cantidad_pagada, fecha):
        if datetime.now() >= self.fecha_inicio:
            print(f"Ya no se puede inscribir a '{self.nombre}', el curso ya ha comenzado.")
            return

        if self.cupos_disponibles <= 0:
            print(f"No hay cupos disponibles para el curso '{self.nombre}'.")
            return

        if cantidad_pagada < self.precio:
            print(f"{usuario.nombre} no pagó suficiente para inscribirse en '{self.nombre}'.")
            return

        descuento = min(usuario.saldo_por_bonos, cantidad_pagada * 0.5)
        cantidad_pagada -= descuento
        usuario.saldo_por_bonos -= descuento

        # Inscripcion
        self.inscripciones.append(usuario)
        usuario.cursos_inscritos.append({'curso': self, 'cantidad_pagada': cantidad_pagada})

        # Actualización de cupos disponibles
        self.cupos_disponibles -= 1

        # Verificacion de bono por inscripciones mínimas
        if len(self.inscripciones) >= self.inscripciones_minimas:
            bono = self.precio * self.bono_porcentaje / 100
            for u in self.inscripciones:
                u.saldo_por_bonos += bono
                print(f"{u.nombre} tiene €{bono} a favor gracias al bono en '{self.nombre}'.")

        print(f"{usuario.nombre} se inscribió en '{self.nombre}' pagando €{cantidad_pagada}.")
        print(f"Cupos disponibles: {self.cupos_disponibles}.")    
    
    
    
    
    
class Usuario:
    def __init__(self, nombre, email, clave):
        self.nombre = nombre
        self.email = email
        self.clave = clave
        self.cursos_inscritos = []
        self.saldo_por_bonos = 0.0
        
    def inscribirseEnCurso(self, curso, cantidad_pagada):
        if curso in self.cursos_inscritos:
            print(f"Ya estas inscrito en el curso '{curso.nombre}.'")
            return
        
        descuento = min(self.saldo_por_bonos, cantidad_pagada * 0.5)
        cantidad_pagada -= descuento
        self.saldo_por_bonos -= descuento
        
        self.cursos_inscritos.append({'curso': curso, 'cantidad_pagada': cantidad_pagada})
        curso.inscribirUsuario(self, cantidad_pagada, datetime.now())
        
        print(f"{self.nombre} se inscribió en '{curso.nombre}' pagando €{cantidad_pagada}.")
        
        if descuento > 0:
            print(f"Se usó un bono de €{descuento}. Nuevo saldo a favor: €{self.saldo_por_bonos}.")
                
            
    def valorarCurso(self, curso, puntaje, comentario):
    
        if curso not in [c['curso'] for c in self.cursos_inscritos]:
            print(f"No puedes valorar '{curso.nombre}' porque no estás inscrito.")
            return
        
        curso.agregarValoracion(puntaje,comentario)
        print(f"{self.nombre} valoró '{curso.nombre}' con {puntaje}/5: '{comentario}'")


    def historial_de_inscripciones(self):
        
        if not self.cursos_inscritos:
            print(f"{self.nombre} aún no se ha inscrito en ningún curso.")
            return

        print(f"Historial de inscripciones de {self.nombre}:")
        for inscripcion in self.cursos_inscritos:
            curso = inscripcion['curso']
            print(f"{curso.nombre}: €{inscripcion['cantidad_pagada']} pagados")


    def agregar_saldo_a_favor(self, cantidad):
        self.saldo_por_bonos += cantidad
        print(f"{self.nombre} ahora tiene €{self.saldo_por_bonos} a favor.")
            


class Valoracion:
    def __init__(self, puntaje, comentario, fecha=None):
        if not (1 <= puntaje <= 5):
            print("El puntaje debe estar entre 1 y 5.")
            return
        
        self.puntaje = puntaje
        self.comentario = comentario
        self.fecha = datetime.now().strftime("%Y-%m-%d")
        
        if fecha is None:
            self.fecha = datetime.now().strftime("%Y-%m-%d")
        else:
            # Validar que la fecha tenga el formato correcto
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
                self.fecha = fecha
            except ValueError:
                raise ValueError("La fecha debe estar en formato YYYY-MM-DD.")

