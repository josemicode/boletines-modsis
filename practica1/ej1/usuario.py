from propiedad import Propiedad
class Usuario:
    def __init__(self):
        self.propiedades = []
    
    def registrarPropiedad(self, coste_noche):
        nueva_propiedad = Propiedad(coste_noche)
        self.propiedades.append(nueva_propiedad)
        pass

    def alquilarPropiedad(self):
        pass

#* Asumimos la capacidad de multipropiedades
#! Clase Sistema que adminisstre entidades y les de formato de antemano