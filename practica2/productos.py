from abc import ABC, abstractmethod
# from enumeraciones import MetodoExtraccion, NivelFrutado
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
        self.metodo_extraccion = None # <<MetodoExtraccion>>
        self.acidez = None # float
        self.cantidad_polifenoles = None # int
        self.color = None # str
        self.defectos_sensoriales = [] # List[DefectoSensorial]
        self.perfil_frutado = None # str
        self.nivel_frutado = None # NivelFrutado
    
    # Setters
    def setMetodoExtraccion(self, metodo):
        self.metodo_extraccion = metodo
    
    def setAcidez(self, acidez):
        self.acidez = acidez
    
    def setCantidadPolifenoles(self, cantidad):
        self.cantidad_polifenoles = cantidad
    
    def setColor(self, color):
        self.color = color
    
    def nuevoDefectoSensorial(self, defecto):
        self.defectos_sensoriales.append(defecto)

    def setPerfilFrutado(self, perfil):
        self.perfil_frutado = perfil

    def setNivelFrutado(self, nivel):
        self.nivel_frutado = nivel
    
    def aceptarAnalizador(self, analizador):
        return analizador.analizarAceite(self)

class Oliva(Producto):
    def __init__(self):
        super().__init__()
    
    def aceptarAnalizador(self, analizador):
        return analizador.analizarOliva(self)