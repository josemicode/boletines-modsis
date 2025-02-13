from datetime import datetime
#import reglas
class Propiedad:
    def __init__(self, coste_noche):
        self.coste_noche = coste_noche
        self.reglas = []
        self.reservas = []
    
    def nuevaRegla(self, regla):
        self.reglas.append(regla)
        self.reglas.sort(key=lambda r: r.prioridad)
    
    def calcularPrecio(self, fecha_inicio, fecha_fin):
        precio = (fecha_fin - fecha_inicio).days * self.coste_noche
        for regla in self.reglas:
            precio += regla.aplicar(fecha_inicio, fecha_fin, precio)
        return precio
    
    def nuevaReserva(self, reserva):
        self.reservas.append(reserva)

    #? Handling de fechas...
    #* Finalmente, se esperaran objetos datetime como parametros; formatear en el main