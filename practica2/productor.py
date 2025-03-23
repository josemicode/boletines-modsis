class Productor:
    def __init__(self, nombre, apellidos, NIF, direccion, telefono, email):
        self._nombre = nombre
        self._apellidos = apellidos
        self._nif = NIF
        self._direccion = direccion
        self._telefono = telefono
        self._email = email

    # Getters
    def getNombre(self):
        return self._nombre
    
    def getApellidos(self):
        return self._apellidos
    
    def getNIF(self):
        return self._nif
    
    def getDireccion(self):
        return self._direccion
    
    def getTelefono(self):
        return self._telefono
    
    def getEmail(self):
        return self._email
    
    def toString(self):
        return f"{self._nombre} {self._apellidos} - ({self._nif})"