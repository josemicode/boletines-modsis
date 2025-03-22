from abc import ABC, abstractmethod
# from enumeraciones import MetodoExtraccion, NivelFrutado, UniformidadColor, PerfilSabor, ProcesoCurado
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
        self.puntaje = None # float
    
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

    # Getters
    def getMetodoExtraccion(self):
        return self.metodo_extraccion

    def getAcidez(self):
        return self.acidez

    def getCantidadPolifenoles(self):
        return self.cantidad_polifenoles

    def getColor(self):
        return self.color

    def getDefectosSensoriales(self):
        return self.defectos_sensoriales

    def getPerfilFrutado(self):
        return self.perfil_frutado

    def getNivelFrutado(self):
        return self.nivel_frutado

    def getPuntaje(self):
        return self.puntaje


class Oliva(Producto):
    def __init__(self):
        super().__init__()
        self.uniformidad_color = None # UniformidadColor
        self.tamano_promedio = None # float
        self.desvio_tamano = None # float
        self.perfil_sabor = None # PerfilSabor
        self.proceso_curado = None # ProcesoCurado
        self.contenido_sal = None # float
        self.porcentaje_defectos_visuales = None # float
        self.ph = None # float
        self.puntaje = None # float

    #Getters
    def getUniformidadColor(self):
        return self.uniformidad_color

    def getTamanoPromedio(self):
        return self.tamano_promedio

    def getDesvioTamano(self):
        return self.desvio_tamano

    def getPerfilSabor(self):
        return self.perfil_sabor

    def getProcesoCurado(self):
        return self.proceso_curado

    def getContenidoSal(self):
        return self.contenido_sal

    def getPorcentajeDefectosVisuales(self):
        return self.porcentaje_defectos_visuales

    def getPh(self):
        return self.ph

    def getPuntaje(self):
        return self.puntaje
    
    # Setters
    def setUniformidadColor(self, uniformidad):
        self.uniformidad_color = uniformidad
    
    def setTamanoPromedio(self, tamano):
        self.tamano_promedio = tamano

    def setDesvioTamano(self, desvio):
        self.desvio_tamano = desvio

    def setPerfilSabor(self, perfil):
        self.perfil_sabor = perfil
    
    def setProcesoCurado(self, proceso):
        self.proceso_curado = proceso

    def setContenidoSal(self, contenido):
        self.contenido_sal = contenido

    def setPorcentajeDefectosVisuales(self, porcentaje):
        self.porcentaje_defectos_visuales = porcentaje
    
    def setPh(self, ph):
        self.ph = ph
    
    def aceptarAnalizador(self, analizador):
        return analizador.analizarOliva(self)