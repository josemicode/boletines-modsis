class Reserva:
    def __init__(self, fecha_inicio, fecha_fin, precio, usuario_asignado):
        self.inicio = fecha_inicio
        self.fin = fecha_fin
        self.precio = precio
        self.usuario_asignado = usuario_asignado
    
    def getFechaInicio(self):
        return self.inicio
    
    def getFechaFin(self):
        return self.fin
    
    def getPrecio(self):
        return self.precio

    def getUsuarioAsignado(self):
        return self.usuario_asignado

    def toString(self):
        return f"Inicio: {self.getFechaInicio()}, Fin: {self.getFechaFin()}, Precio: {self.getPrecio()}, Usuario: {self.getUsuarioAsignado().getNombre()}"