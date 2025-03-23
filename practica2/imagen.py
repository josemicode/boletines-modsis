class Imagen:
    def __init__(self, ruta):
        self.ruta = ruta
        self.analisis = None # AnalisisImagen

    def getRuta(self):
        return self.ruta
    
    def getAnalisis(self):
        return self.analisis
    
    def setAnalisis(self, analisis_imagen):
        self.analisis = analisis_imagen