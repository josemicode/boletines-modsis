from propiedad import Propiedad
from sistema import Sistema
class Usuario:
    def __init__(self):
        self.propiedades = []
    
    def registrarPropiedad(self, coste_noche):
        Sistema().registrar(self, coste_noche)

    def alquilarPropiedad(self, propiedad, fecha_inicio, fecha_fin):
        return Sistema().alquilar(propiedad, fecha_inicio, fecha_fin)
    
    def asignarRegla(self, nueva_regla, propiedad):
        #if propiedad in self.propiedades:
        Sistema().introducirRegla(nueva_regla, propiedad)
'''
    def listarPropiedades(self):
        for propiedad in self.propiedades:
            print()
'''