from directorio import Directorio

class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.directorios = []
    
    def crearDirectorio(self, nombre, ruta):
        if ruta == "":
            pass

    def getNumArchivos(self):
        pass

    def getTamanoTotal(self):
        pass

#? Muy posible el futuro encapsulamiento por una entidad handler Sistema