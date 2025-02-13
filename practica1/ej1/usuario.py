from propiedad import Propiedad
class Usuario:
    def __init__(self, identificador):
        self.id = identificador
        self.propiedades = []
    
    def registrarPropiedad(self, coste_noche):
        id_generado = self.id + str(len(self.propiedades))
        nueva_propiedad = Propiedad(id_generado, coste_noche)
        self.propiedades.append(nueva_propiedad)
        pass

    def alquilarPropiedad(self):
        pass

#* Asumimos la capacidad de multipropiedades