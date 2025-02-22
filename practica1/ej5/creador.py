# Registrar nuevo creador de recursos: se indica su nombre, email,  
# contraseña y se inicia con 0 su cantidad de puntos.
class Creador:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.puntos = 0

    def getNombre(self):
        return self.nombre
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def getPuntos(self):
        return self.puntos
    
    def sumarPuntos(self, puntos):
        self.puntos += puntos

    def __str__(self):
        return f"Creador: nombre - {self.nombre}, email - {self.email}, puntos - {self.puntos}"