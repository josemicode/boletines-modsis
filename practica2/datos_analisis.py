class AnalisisImagen:
    # Constructor
    # tipo_analisis: string
    # datos_analisis: List[DatoAnalisis]
    def __init__(self, tipo_analisis, datos_analisis):
        self._tipo_analisis = tipo_analisis
        self._analisis = []
    
    def getTipoAnalisis(self):
        return self._tipo_analisis
    
    def getAnalisis(self):
        return self._analisis
    
    # def nuevoAnalisis(self, analisis):
    #     self._analisis.append(analisis)

class DatoAnalisis:
    # Constructor
    # nombre: string
    # valor: float
    def __init__(self, nombre, valor):
        self._nombre = nombre
        self._valor = valor
    
    def getNombre(self):
        return self._nombre
    
    def getValor(self):
        return self._valor