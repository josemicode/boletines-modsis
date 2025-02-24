from estrategias import Oferta
# Registrar una nueva compra de recurso: se indica el usuario y el recurso a adquirir
class Compra:
    def __init__(self, usuario, recurso, fecha):
        self.usuario = usuario
        self.recurso = recurso
        self.fecha = fecha
        #? Podria calcular el costo y los puntos en el constructor
        self.coste = self.calcularCoste()
        self.recurso.vender()
        self.puntos = self.calcularPuntos()
        self.recurso.getCreador().sumarPuntos(self.puntos)
    
    def getUsuario(self):
        return self.usuario
    
    def getRecurso(self):
        return self.recurso
    
    def getFecha(self):
        return self.fecha
    
    def calcularCoste(self):
        estrategia = self.getRecurso().getEstrategia()
        precio_base = self.getRecurso().getPrecioBase()

        if isinstance(estrategia, Oferta):
            return estrategia.calcularCoste(precio_base, self.getFecha())
        
        return estrategia.calcularCoste(precio_base)
    
    def calcularPuntos(self):
        estrategia = self.getRecurso().getEstrategia()
        precio_base = self.getRecurso().getPrecioBase()

        if isinstance(estrategia, Oferta):
            return estrategia.calcularPuntos(precio_base, self.getFecha())
        
        return estrategia.calcularPuntos(precio_base)
    
    def __str__(self):
        return f"Compra: usuario - {self.usuario.getNombre()}, recurso - {self.recurso.getDescripcion()}, fecha - {self.fecha}, coste - {self.coste}, puntos - {self.puntos})"