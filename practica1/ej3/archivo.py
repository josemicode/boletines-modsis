class Archivo:
    def __init__(self, nombre, fecha_creacion):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_creacion
        self.tamano = 10 #! demo
    
    def getNombre(self):
        return self.nombre
    
    def getFechaCreacion(self):
        return self.fecha_creacion
    
    def getFechaModificacion(self):
        return self.fecha_modificacion
    
    def getTamano(self):
        return self.tamano