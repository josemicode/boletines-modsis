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
            self.directorios.append(Directorio(nombre))
            return True
        
        dir = self.tieneDirectorio(separados[1])
        if dir.getNombre() == "":
            return False
        
        nueva_ruta = "/".join(separados[1:])
        return dir.crearDirectorio(nombre, nueva_ruta)
    
    #! Asumo que funciona :)