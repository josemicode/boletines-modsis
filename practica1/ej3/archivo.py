class Archivo:
    def __init__(self, nombre, fecha_creacion, propietario):
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_creacion
        self.propietario = propietario
        self.tamano = 10 #! demo
        #* Atributos de control de permisos
        self.fecha_caducidad = None
        self.permitidos = []
    
    def getNombre(self):
        return self.nombre
    
    def getFechaCreacion(self):
        return self.fecha_creacion
    
    def getFechaModificacion(self):
        return self.fecha_modificacion
    
    def getTamano(self):
        return self.tamano
    
    def publicar(self, fecha_caducidad):
        self.fecha_caducidad = fecha_caducidad

    def compartirCon(self, usuario):
        if usuario not in self.permitidos:
            self.permitidos.append(usuario)
    
    def tienePermiso(self, usuario, fecha):
        if usuario == self.propietario:
            return True

        if self.fecha_caducidad != None:
            if fecha > self.fecha_caducidad:
                return False
            return True
        
        if usuario in self.permitidos:
            return True
        return False