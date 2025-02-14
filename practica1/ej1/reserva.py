class Reserva:
    def __init__(self, fecha_inicio, fecha_fin, precio):
        self.inicio = fecha_inicio
        self.fin = fecha_fin
        self.precio = precio
    
    def getFechaInicio(self):
        return self.inicio
    
    def getFechaFin(self):
        return self.fin
    
    def getPrecio(self):
        return self.precio