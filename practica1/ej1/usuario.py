from propiedad import Propiedad
from sistema import Sistema
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.propiedades = []
    
    def registrarPropiedad(self, nueva_propiedad):
        self.propiedades.append(nueva_propiedad)

    def getNombre(self):
        return self.nombre

    #def alquilarPropiedad(self, propiedad, fecha_inicio, fecha_fin):
        # return Sistema().alquilar(propiedad, fecha_inicio, fecha_fin)
    
    #def asignarRegla(self, nueva_regla, propiedad):
        ##if propiedad in self.propiedades:
        #return Sistema().introducirRegla(nueva_regla, propiedad)
'''
    def listarPropiedades(self):
        for propiedad in self.propiedades:
            print()
'''