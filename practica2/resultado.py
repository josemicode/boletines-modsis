class Resultado:
    # nombre: str
    # fecha_hora: datetime
    # atributos: list[AtributoResultado]
    def __init__(self, nombre, fecha_hora, atributos):
        self._nombre = nombre
        self._fecha_hora = fecha_hora
        self._atributos = atributos
    
    # Getters
    def getNombre(self):
        return self._nombre
    
    def getFechaHora(self):
        return self._fecha_hora
    
    def getAtributos(self):
        return self._atributos