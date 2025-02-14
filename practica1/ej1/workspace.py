from datetime import date
from usuario import Usuario
from reglas import ReglaRango, ReglaProlongacion
#from propiedad import *

def main():
    #* Usuarios y registro de propiedades
    usuario1 = Usuario()
    usuario1.registrarPropiedad(10)
    usuario1.registrarPropiedad(20)
    propiedad1 = usuario1.propiedades[0]
    propiedad2 = usuario1.propiedades[1]
    #print(propiedad1.coste_noche)
    usuario2 = Usuario()

    #* Reglas de rango de fechas
    regla1 = ReglaRango(-0.5, date(2025, 5, 5), date(2025, 5, 10))
    asignacion1 = usuario1.asignarRegla(regla1, propiedad1)
    print("Regla 1 asignada? ", asignacion1)
    regla2 = ReglaRango(0.1, date(2025, 2, 1), date(2025, 6, 4))
    asignacion2 = usuario1.asignarRegla(regla2, propiedad1)
    print("Regla 2 asignada? ", asignacion2)
    regla3 = ReglaRango(0.1, date(2025, 2, 1), date(2025, 2, 6))
    asignacion3 = usuario1.asignarRegla(regla3, propiedad1)
    print("Regla 3 asignada? ", asignacion3)

    #* Reglas por estancia prolongada
    regla4 = ReglaProlongacion(-0.2, 15)
    asignacion4 = usuario1.asignarRegla(regla4, propiedad1)
    print("Regla 4 asignada? ", asignacion4)
    regla5 = ReglaProlongacion(-0.3, 30)
    asignacion5 = usuario1.asignarRegla(regla5, propiedad1)
    print("Regla 5 asignada? ", asignacion5, "\n")

    #* Alquiler

    proceso1 = usuario2.alquilarPropiedad(propiedad1, date(2025, 2, 5), date(2025, 2, 10))
    print("Reserva 1 completada? ", proceso1)
    reserva1 = propiedad1.reservas[0]
    print("Inicio: ", reserva1.getFechaInicio())
    print("Fin: ", reserva1.getFechaFin())
    print("Precio: ", reserva1.getPrecio(), "\n")

    proceso2 = usuario2.alquilarPropiedad(propiedad1, date(2025, 1, 29), date(2025, 2, 6))
    print("Reserva 2 completada? ", proceso2, "\n")

    proceso3 = usuario2.alquilarPropiedad(propiedad1, date(2025, 5, 5), date(2025, 5, 25))
    print("Reserva 3 completada? ", proceso3)
    reserva2 = propiedad1.reservas[1]
    print("Inicio: ", reserva2.getFechaInicio())
    print("Fin: ", reserva2.getFechaFin())
    print("Precio: ", reserva2.getPrecio(), "\n")

if __name__ == "__main__":
    main()