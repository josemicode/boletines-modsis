from directorio import Directorio

class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.directorios = []

    def getPrimerDirectorio(self, ruta):
        separados = ruta.split("/")
        return separados[0]

    def directorioValido(self, ruta):
        primero = self.getPrimerDirectorio(ruta)
        for dir in self.directorios:
            if primero == dir.getNombre():
                return dir
        return Directorio("")
    
    def crearDirectorio(self, nombre, ruta):
        if ruta == "":
            self.directorios.append(Directorio(nombre))
            return True
        
        dir = self.directorioValido(ruta)
        if dir.getNombre() == "":
            return False
        
        return dir.crearDirectorio(nombre, ruta)

    def getNumArchivos(self):
        pass

    def getTamanoTotal(self):
        pass

#? Muy posible el futuro encapsulamiento por una entidad handler Sistema