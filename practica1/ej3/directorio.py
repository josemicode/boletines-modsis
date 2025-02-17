from archivo import Archivo
from datetime import date
class Directorio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.directorios = []
        self.archivos = []
    
    def getNombre(self):
        return self.nombre
    
    def tieneDirectorio(self, nombre):
        for dir in self.directorios:
            if nombre == dir.getNombre():
                return dir
        return Directorio("")
    
    #FIXME: impedir dirs duplicados
    def crearDirectorio(self, nombre, ruta):
        separados = ruta.split("/")
        if len(separados) == 1:
            if self.tieneDirectorio(nombre).getNombre() == "":
                self.directorios.append(Directorio(nombre))
                return True
            return False
        
        dir = self.tieneDirectorio(separados[1])
        if dir.getNombre() == "":
            return False
        
        nueva_ruta = "/".join(separados[1:])
        return dir.crearDirectorio(nombre, nueva_ruta)
    
    def tieneArchivo(self, nombre):
        for ar in self.archivos:
            if nombre == ar.getNombre():
                return ar
        return Archivo("", date(1, 1, 1))
    
    def crearArchivo(self, nombre, fecha_creacion, ruta):
        separados = ruta.split("/")
        if len(separados) == 1:
            if self.tieneArchivo(nombre).getNombre() == "":
                self.archivos.append(Archivo(nombre, fecha_creacion))
                return True
            return False
        
        dir = self.tieneDirectorio(separados[1])
        if dir.getNombre() == "":
            return False
        
        nueva_ruta = "/".join(separados[1:])
        return dir.crearArchivo(nombre, fecha_creacion, nueva_ruta)
    
    def getNumArchivos(self):
        contador = 0
        for ar in self.archivos:
            contador += 1

        for dir in self.directorios:
            contador += dir.getNumArchivos()
        
        return contador
    
    def getTamanoTotal(self):
        tam = 0
        for ar in self.archivos:
            tam += ar.getTamano()

        for dir in self.directorios:
            tam += dir.getTamanoTotal()
        return tam