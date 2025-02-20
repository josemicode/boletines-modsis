# Registrar un proyecto: Se indica el nombre, la descripción, la fecha hasta
# la que se aceptan ofertas.
class Proyecto:
    def __init__(self, nombre, descripcion, fecha_limite):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite