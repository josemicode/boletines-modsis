class DefectoSensorial:
    def __init__(self, comentario, nivel_gravedad):
        self.comentario = comentario # str
        self.gravedad = nivel_gravedad # int
    
    # Getters
    def getComentario(self):
        return self.comentario
    
    def getGravedad(self):
        return self.gravedad