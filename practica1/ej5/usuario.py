# Registrar nuevo usuario: se indica su nombre, email y contraseña.
class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.biblioteca = []
        #? Necesario decidir si se necesita una lista de descargas o si simplemente habra un metodo que comprube si un recurso puede ser descargado
        self.urls = []

    def getNombre(self):
        return self.nombre
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getBiblioteca(self):
        return self.biblioteca
    
    def getUrls(self):
        return self.urls
    
    def nuevoRecurso(self, recurso):
        self.biblioteca.append(recurso)
    
    def nuevaUrl(self, url):
        self.urls.append(url)

    #! Delegar a Sistema como descargable(usuario, recurso)
    # def descargarRecurso(self, recurso):
    #     if recurso not in self.getBiblioteca() or recurso in self.getDescargas():
    #         return False
        
    #     if recurso.getEstrategia().descargable(recurso.getVentas()):
    #         self.descargas.append(recurso)
    #         return True
    #     return False

    def __str__(self):
        return f"Usuario: nombre - {self.nombre}, email - {self.email}"