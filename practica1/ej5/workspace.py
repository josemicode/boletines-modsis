from datetime import date
from creador import Creador
from recurso import Recurso
from usuario import Usuario
from compra import Compra
from estrategias import Oferta, CrowdBased, Normal
from sistema import Sistema
'''
Una empresa requiere una plataforma para que diseñadores y creadores
puedan comercializar por allí sus diseños y recursos (imágenes, íconos,
tipografías, templates web, etc.). Cada vez que un creador de recursos registra
una nueva producción, puede configurar una estrategia de comercialización, que
son ideadas por los propietarios de la plataforma. Los creadores de recursos
juntan puntos cada vez que un usuario adquiere uno de sus productos. Y estos
puntos sirven a la plataforma no solo para posicionar a los creadores dentro de
la misma sino también para computar su costo de suscripción a la plataforma en
un futuro.
'''

def main():
    #* Crear creadores
    creador1 = Creador("emilio32", "emilio32@gmail.com", "123456")
    creador2 = Creador("DaVinci101", "davincicode@hotmail.com", "gsdgsgh_sowhfwe8")
    
    #* Crear estrategias
    estrategia1 = Normal()
    estrategia2 = Oferta(0.2, date(2023, 12, 31))
    estrategia3 = CrowdBased(2)

    #* Crear recursos
    recurso1 = Recurso(creador1, "R1", "test.png", "ejemplo.com", date.today(), 100, estrategia1)
    recurso2 = Recurso(creador2, "R2", "gatito.png", "2432/fotosdegatos.es", date.today(), 200, estrategia2)
    recurso3 = Recurso(creador1, "R3", "chart.png", "plane55/charts.com", date.today(), 300, estrategia3)

    #* Crear usuarios
    usuario1 = Usuario("pokemaster", "poke@master.com", "gottacatchemall")
    usuario2 = Usuario("Rocket", "rck99@gmail.com", "aaaa")

    #* Registrar compras
    compra1 = Compra(usuario1, recurso1, date.today())
    compra2 = Compra(usuario2, recurso2, date(2023, 11, 30)) 
    compra3 = Compra(usuario1, recurso3, date.today())

    #* Mostrar resultados
    print(creador1)
    print(creador2)
    print(recurso1)
    print(recurso2)
    print(recurso3)
    print(usuario1)
    print(usuario2)
    print(compra1)
    print(compra2)
    print(compra3)
    print()

    print("Puntos de creador1:", creador1.getPuntos())
    print("Puntos de creador2:", creador2.getPuntos())

    print("\nBiblioteca de usuario1: ")
    for rec in usuario1.getBiblioteca():
        print(rec)

    print("\nBiblioteca de usuario2: ")
    for rec in usuario2.getBiblioteca():
        print(rec)

    print("\nUrls de usuario1: ")
    for rec in usuario1.getBiblioteca():
        Sistema().recursoDescargablePor(rec, usuario1)
    for url in usuario1.getUrls():
        print(url)

    print("\nUrls de usuario2: ")
    for rec in usuario2.getBiblioteca():
        Sistema().recursoDescargablePor(rec, usuario2)
    for url in usuario2.getUrls():
        print(url)
    
    #* Comprobacion adicional de crowd-based
    print("\nComprobamos que R3 se pueda descargar al llegar al cupo de ventas (2)")
    compra4 = Compra(usuario2, recurso3, date.today())
    Sistema().recursoDescargablePor(recurso3, usuario1)
    print("Urls de usuario1: ")
    for url in usuario1.getUrls():
        print(url)

if __name__ == "__main__":
    main()