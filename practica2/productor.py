class Productor:
    def __init__(self, nombre, apellidos, NIF, direccion, telefono, email):
        self._nombre = nombre
        self._apellidos = apellidos
        self._nif = NIF
        self._direccion = direccion
        self._telefono = telefono
        self._email = email
     # Una pregunta jose, los atributos en python no eran "nombre" es publico, "_nombre" es protegido y "__nombre" es privado?
     # No me eches mucha cuenta pero me suena de haberlo escuchado así
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