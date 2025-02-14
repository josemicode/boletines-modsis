from propiedad import Propiedad
from reserva import Reserva
class Sistema:
    def __init__(self):
        pass

    def registrar(self, usuario, coste):
        nueva_propiedad = Propiedad(coste)
        usuario.propiedades.append(nueva_propiedad)

    def reservaViable(self, propiedad, fecha_inicio, fecha_fin):
        for reserva in propiedad.reservas:
            menor = max(reserva.inicio, fecha_inicio)
            mayor = min(reserva.fin, fecha_fin)
            if menor <= mayor:
                return False
        return True
    
    #? Alquilar podria asociar el usuario a la reserva tambien
    def alquilar(self, propiedad, fecha_inicio, fecha_fin):
        if self.reservaViable(propiedad, fecha_inicio, fecha_fin):
            precio = propiedad.calcularPrecio(fecha_inicio, fecha_fin)
            reserva = Reserva(fecha_inicio, fecha_fin, precio)
            propiedad.nuevaReserva(reserva)
            return True
        return False

    def noExisteReglaRango(self, nueva_regla, propiedad):
        for regla in propiedad.reglas:
            if regla.prioridad == 1:
                menor = max(regla.inicio, nueva_regla.inicio)
                mayor = min(regla.fin, nueva_regla.fin)
                if menor <= mayor:
                    return False
        return True
    
    def noExisteReglaProlongacion(self, propiedad):
        for regla in propiedad.reglas:
            if regla.prioridad == 2:
                return False
        return True

    def introducirRegla(self, nueva_regla, propiedad):
        if nueva_regla.prioridad == 1:
            aplicable = self.noExisteReglaRango(nueva_regla, propiedad)
        elif nueva_regla.prioridad == 2:
            aplicable = self.noExisteReglaProlongacion(propiedad)

        if aplicable:
            propiedad.nuevaRegla(nueva_regla)
            return True
        return False