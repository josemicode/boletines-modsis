# Registrar nuevo usuario: se indica su nombre, email y contraseña.
class Usuario:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def getNombre(self):
        return self.nombre
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password