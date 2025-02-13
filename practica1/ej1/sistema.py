from propiedad import Propiedad
class Sistema:
    def __init__(self):
        pass

    def registrar(self, usuario, coste):
        nueva_propiedad = Propiedad(coste)
        usuario.propiedades.append(nueva_propiedad)
    
    def alquilar(self, propiedad):
        pass

    def introducirRegla(self, regla, propiedad):
        pass