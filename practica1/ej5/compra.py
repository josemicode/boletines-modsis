# Registrar una nueva compra de recurso: se indica el usuario y el recurso a adquirir
class Compra:
    def __init__(self, usuario, recurso):
        self.usuario = usuario
        self.recurso = recurso
        #? Podria calcular el costo y los puntos en el constructor
        #self.costo = self.calcular_costo()
        #self.puntos = self.calcular_puntos()