from propiedad import Propiedad
from reserva import Reserva
class Sistema:
    def __init__(self):
        pass

    def crearPropiedadPara(self, usuario, coste):
        nueva_propiedad = Propiedad(coste)
        usuario.registrarPropiedad(nueva_propiedad)

    #? Alquilar podria asociar el usuario a la reserva tambien
    def alquilar(self, propiedad, usuario, fecha_inicio, fecha_fin):
        if propiedad.reservaViable(fecha_inicio, fecha_fin):
            precio = propiedad.calcularPrecio(fecha_inicio, fecha_fin)
            reserva = Reserva(fecha_inicio, fecha_fin, precio, usuario)
            propiedad.nuevaReserva(reserva)
            return True
        return False