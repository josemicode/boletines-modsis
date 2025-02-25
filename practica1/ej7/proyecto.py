# Registrar un proyecto: Se indica el nombre, la descripción, la fecha hasta
# la que se aceptan ofertas.
class Proyecto:
    def __init__(self, nombre, descripcion, fecha_limite, categoria, ofertas_disponibles):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.categoria = categoria
        self.ofertas_disponibles = ofertas_disponibles
        self.oferta_final = None
        # self.freelancer = None #! Innecesario, oferta ahora conoce a un freelancer

    def getNombre(self):
        return self.nombre

    def getDescripcion(self):
        return self.descripcion

    def getFechaLimite(self):
        return self.fecha_limite

    def getCategoria(self):
        return self.categoria

    def asignarOferta(self, oferta, fecha_asignacion):
        if self.oferta_final is None and fecha_asignacion <= self.fecha_limite:
            self.oferta_final = oferta
            return True
        return False

    def getOfertaFinal(self):
        return self.oferta_final

    # def getFreelancer(self):
    #     return self.freelancer
    
    # def asignarFreelancer(self, freelancer):
    #     self.freelancer = freelancer

    def getOfertas(self):
        return self.ofertas_disponibles

    #* Esta funcion lambda ordena las ofertas por puntaje de mayor a menor
    def ordenarOfertasPorPuntaje(self):
        self.ofertas_disponibles.sort(key=lambda oferta: oferta.getPuntaje(), reverse=True) 

    def finalizar(self):
        if self.oferta_final is None:
            return False
        self.fecha_finalizacion = self.oferta_final.getFechaEntrega()
        puntaje = self.oferta_final.getPuntaje()
        self.oferta_final.getFreelancer().sumarPuntaje(puntaje)
        #? Por que no hacerlo en el metodo getPuntaje? La respuesta es que no al ordenar las ofertas por puntaje, se recalcula el puntaje de cada oferta
        #? en otras palabras, cada vez que se pidiera una lista de recomendaciones, el freelancer sumaria puntos por cada oferta en la que se encuentre
        return True

    def __str__(self):
        return f"Proyecto: nombre - {self.nombre}, descripcion - {self.descripcion}, fecha limite - {self.fecha_limite}"