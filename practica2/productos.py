from abc import ABC, abstractmethod
import random

class Producto(ABC):
    def __init__(self):
        self.cantidad_producida = 0
        self.unidad_cantidad = ""
        self.codigo = self._codeGen()

    def _codeGen(self):
        for i in range(20):
            res += str(random.randint(0, 9))
        return res
    
    @abstractmethod
    def aceptarAnalizador(self, analizador):
        pass
    #? Puntaje calculado aqui? Ya veremos...


class Aceite(Producto):
    def __init__(self):
        super().__init__()
    
    def aceptarAnalizador(self, analizador):
        return analizador.analizarAceite(self)

class Oliva(Producto):
    def __init__(self):
        super().__init__()
    
    def aceptarAnalizador(self, analizador):
        return analizador.analizarOliva(self)