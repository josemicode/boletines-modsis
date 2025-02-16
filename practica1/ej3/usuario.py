from directorio import Directorio

class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.directorios = []

    # def getPrimerDirectorio(self, ruta):
    #     separados = ruta.split("/")
    #     return separados[0]

    def existeDirectorio(self, nombre):
        for dir in self.directorios:
            if nombre == dir.getNombre():
                return dir
        return Directorio("")

    def directorioValido(self, ruta):
        separados = ruta.split("/")
        primero = separados[0]
        return self.existeDirectorio(primero)
    
    def crearDirectorio(self, nombre, ruta):
        if ruta == "":
            if self.existeDirectorio(nombre).getNombre() == "":
                self.directorios.append(Directorio(nombre))
                return True
            return False
        
        dir = self.directorioValido(ruta)
        if dir.getNombre() == "":
            return False
        return dir.crearDirectorio(nombre, ruta)
    
    def crearArchivo(self, nombre, fecha_creacion, ruta):
        dir = self.directorioValido(ruta)
        if dir.getNombre() == "":
            return False
        return dir.crearArchivo(nombre, fecha_creacion, ruta)

    def getNumArchivos(self):
        pass

    def getTamanoTotal(self):
        pass

#? Muy posible el futuro encapsulamiento por una entidad handler Sistema