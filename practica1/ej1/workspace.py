from datetime import date
from sistema import Sistema
from usuario import Usuario
from reglas import ReglaRango, ReglaProlongacion
from propiedad import Propiedad


def main():
    #* Usuarios y registro de propiedades
    sistema = Sistema()
    usuario1 = Usuario("Pepe")
    sistema.crearPropiedadPara(usuario1, 10)
    sistema.crearPropiedadPara(usuario1, 20)
    propiedad1 = usuario1.propiedades[0]
    propiedad2 = usuario1.propiedades[1]
    
    #print(propiedad1.coste_noche)
    usuario2 = Usuario("Manuel")

    #* Reglas de rango de fechas
    regla1 = ReglaRango(-0.5, date(2025, 5, 5), date(2025, 5, 10))
    asignacion1 = propiedad1.introducirRegla(regla1)
    print("Regla 1 asignada? ", asignacion1)
    regla2 = ReglaRango(0.1, date(2025, 2, 1), date(2025, 6, 4))
    asignacion2 = propiedad1.introducirRegla(regla2)
    print("Regla 2 asignada? ", asignacion2)
    regla3 = ReglaRango(0.1, date(2025, 2, 1), date(2025, 2, 6))
    asignacion3 = propiedad1.introducirRegla(regla3)
    print("Regla 3 asignada? ", asignacion3)

    #* Reglas por estancia prolongada
    regla4 = ReglaProlongacion(-0.2, 15)
    asignacion4 = propiedad1.introducirRegla(regla4)
    print("Regla 4 asignada? ", asignacion4)
    regla5 = ReglaProlongacion(-0.3, 30)
    asignacion5 = propiedad1.introducirRegla(regla5)
    print("Regla 5 asignada? ", asignacion5, "\n")

    #* Alquiler
    proceso1 = sistema.alquilar(propiedad1, usuario2, date(2025, 2, 5), date(2025, 2, 10))
    print("Reserva 1 completada? ", proceso1)
    reserva1 = propiedad1.reservas[0]
    print(reserva1.toString(), "\n")

    proceso2 = sistema.alquilar(propiedad1, usuario2, date(2025, 1, 29), date(2025, 2, 6))
    print("Reserva 2 completada? ", proceso2, "\n")

    proceso3 = sistema.alquilar(propiedad1, usuario2, date(2025, 5, 5), date(2025, 5, 25))
    print("Reserva 3 completada? ", proceso3)
    reserva2 = propiedad1.reservas[1]
    print(reserva2.toString(), "\n")

if __name__ == "__main__":
    main()