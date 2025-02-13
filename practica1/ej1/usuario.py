from propiedad import Propiedad
from sistema import Sistema
class Usuario:
    def __init__(self):
        self.propiedades = []
    
    def registrarPropiedad(self, coste_noche):
        Sistema().registrar(self, coste_noche)

    def alquilarPropiedad(self, propiedad):
        Sistema().alquilar(self, propiedad)

#* Asumimos la capacidad de multipropiedades
#! Clase Sistema que adminisstre entidades y les de formato de antemano