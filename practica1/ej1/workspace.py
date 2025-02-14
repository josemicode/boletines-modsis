from datetime import date
from usuario import Usuario
#from propiedad import *

def main():
    usuario1 = Usuario()
    usuario1.registrarPropiedad(10)
    usuario1.registrarPropiedad(20)
    propiedad1 = usuario1.propiedades[0]
    propiedad2 = usuario1.propiedades[1]
    #print(propiedad1.coste_noche)
    usuario2 = Usuario()

    proceso1 = usuario2.alquilarPropiedad(propiedad1, date(2025, 2, 5), date(2025, 2, 10))
    print("Reserva 1 completada? ", proceso1)
    reserva1 = propiedad1.reservas[0]
    print("Inicio: ", reserva1.getFechaInicio())
    print("Fin: ", reserva1.getFechaFin())
    print("Precio: ", reserva1.getPrecio())

    proceso2 = usuario2.alquilarPropiedad(propiedad1, date(2025, 1, 29), date(2025, 2, 6))
    print("Reserva 2 completada? ", proceso2)

    proceso3 = usuario2.alquilarPropiedad(propiedad1, date(2025, 5, 5), date(2025, 5, 25))
    print("Reserva 3 completada? ", proceso3)
    reserva2 = propiedad1.reservas[1]
    print("Inicio: ", reserva2.getFechaInicio())
    print("Fin: ", reserva2.getFechaFin())
    print("Precio: ", reserva2.getPrecio())

if __name__ == "__main__":
    main()