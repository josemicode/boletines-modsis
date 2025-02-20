#from datetime import datetime
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
            valor_regla = regla.aplicar(fecha_inicio, fecha_fin, self.coste_noche, precio)
            if valor_regla != 0:
                precio = valor_regla
        return precio

    def nuevaReserva(self, reserva):
        self.reservas.append(reserva)

    def reservaViable(self, fecha_inicio, fecha_fin):
        for reserva in self.reservas:
            menor = max(reserva.inicio, fecha_inicio)
            mayor = min(reserva.fin, fecha_fin)
            if menor <= mayor:
                return False
        return True

    def noExisteReglaRango(self, nueva_regla):
        for regla in self.reglas:
            if regla.prioridad == 1:
                menor = max(regla.inicio, nueva_regla.inicio)
                mayor = min(regla.fin, nueva_regla.fin)
                if menor <= mayor:
                    return False
        return True

    def noExisteReglaProlongacion(self):
        for regla in self.reglas:
            if regla.prioridad == 2:
                return False
        return True

    def introducirRegla(self, nueva_regla):
        if nueva_regla.prioridad == 1:
            aplicable = self.noExisteReglaRango(nueva_regla)
        elif nueva_regla.prioridad == 2:
            aplicable = self.noExisteReglaProlongacion()

        if aplicable:
            self.reglas.append(nueva_regla)
            return True
        return False

    #? Handling de fechas...
    #* Finalmente, se esperaran objetos datetime como parametros; formatear en el main