from ej4 import *


def main():
    # Crear estaciones
    estacion1 = Estacion("Estación de montequinto", 10, 5, 5)
    estacion2 = Estacion("Estación de olivar de quintos", 10, 2, 8)
    estacion3 = Estacion("Estación de Pablo Olavide", 10, 0, 10)  # Estación sin bicicletas disponibles
    estacion4 = Estacion("Estación de Loyola", 10, 5, 0)  # Estación sin estacionamientos disponibles
    
    # Crear usuarios
    usuario1 = Usuario("12345678A", "Juan", "1234-5678-9876-5432")
    usuario2 = Usuario("23456789B", "Ana", "2345-6789-8765-4321")
    
    # Crear abonos para los usuarios
    abono_anual = AbonoAnual(datetime(2023, 1, 1))
    abono_prepago = AbonoPrepago(50)  #saldo de 50€
  
    # Registrar los abonos
    print("\nRegistrando abonos...")
    usuario1.RegistrarAbono(abono_anual)
    usuario2.RegistrarAbono(abono_prepago)
    
    # recoger bicicletas
    print("\nRecogiendo bicicletas:")
    usuario1.RecogerBicicleta(estacion1)  # Usuario 1 recoge una bicicleta de la estación 1
    usuario2.RecogerBicicleta(estacion2)  # Usuario 2 recoge una bicicleta de la estación 2
    
    # devolver las bicicletas después de un tiempo de uso
    print("\nDevolviendo las bicicletas:")
    tiempo_uso_juan = 40  
    tiempo_uso_ana = 60  
    
    usuario1.devolverBicicleta(estacion1, tiempo_uso_juan) 
    usuario2.devolverBicicleta(estacion2, tiempo_uso_ana)  
    
    # Mostrar estaciones con bicicletas disponibles
    print("\nEstaciones con bicicletas disponibles:")
    estaciones_con_bicicletas = Estacion.estaciones_con_bicicletas_disponibles([estacion1, estacion2, estacion3, estacion4])
    for estacion in estaciones_con_bicicletas:
        print(f"- {estacion.ubicacion}")
    
    # Mostrar estaciones con estacionamientos disponibles
    print("\nEstaciones con estacionamientos disponibles:")
    estaciones_con_estacionamientos = Estacion.estaciones_con_estacionamientos_libres([estacion1, estacion2, estacion3, estacion4])
    for estacion in estaciones_con_estacionamientos:
        print(f"- {estacion.ubicacion}")


if __name__ == "__main__":
    main()
