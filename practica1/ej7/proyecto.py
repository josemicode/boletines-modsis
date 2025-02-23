# Registrar un proyecto: Se indica el nombre, la descripción, la fecha hasta
# la que se aceptan ofertas.
class Proyecto:
    def __init__(self, nombre, descripcion, fecha_limite, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.categoria = categoria
        self.oferta = None
        self.freelancer = None

    def getNombre(self):
        return self.nombre
    
    def getDescripcion(self):
        return self.descripcion
    
    def getFechaLimite(self):
        return self.fecha_limite

    def getCategoria(self):
        return self.categoria
    
    def asignarOferta(self, oferta, fecha_asignacion):
        if self.oferta != None and fecha_asignacion < self.fecha_limite:
            self.oferta = oferta
            return True
        return False
    
    def getOferta(self):
        return self.oferta
    
    def getFreelancer(self):
        return self.freelancer
    
    def asignarFreelancer(self, freelancer):
        self.freelancer = freelancer
    
    def finalizar(self, fecha_finalizacion, puntaje):
        self.fecha_finalizacion = fecha_finalizacion
        self.getFreelancer().sumarPuntaje(puntaje)