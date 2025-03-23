from abc import ABC, abstractmethod
from enumeraciones import MetodoExtraccion, NivelFrutado, UniformidadColor, PerfilSabor, ProcesoCurado, Calidad, ResistenciaTermica
import random

class Producto(ABC):
    def __init__(self):
        self.cantidad_producida = 0
        self.unidad_cantidad = ""
        self.lugar_almacenaje = None # str
        self.codigo = self._codeGen()
        self.puntaje = None # float
        self.calidad = None # <<Calidad>>

    def _codeGen(self):
        for i in range(20):
            res += str(random.randint(0, 9))
        return res
    
    # Getters
    def getCantidadProducida(self):
        return self.cantidad_producida
    
    def getUnidadCantidad(self):
        return self.unidad_cantidad
    
    def getLugarAlmacenaje(self):
        return self.lugar_almacenaje
    
    def getCodigo(self):
        return self.codigo

    def getPuntaje(self):
        return self.puntaje

    def setCantidadProducida(self, cantidad):
        self.cantidad_producida = cantidad
    
    def setUnidadCantidad(self, unidad):
        self.unidad_cantidad = unidad
    
    def setLugarAlmacenaje(self, lugar):
        self.lugar_almacenaje = lugar

    def calcularCalidad(self):
        if self.puntaje > 8:
            self.calidad = Calidad.ALTA
        elif 5 <= self.puntaje <= 8:
            self.calidad = Calidad.MEDIA
        else:
            self.calidad = Calidad.BAJA            
    
    @abstractmethod
    def aceptarAnalizador(self, analizador):
        pass
    #? Puntaje calculado aqui? Ya veremos...

    @abstractmethod
    def calcularPuntaje(self):
        pass


class Aceite(Producto):
    def __init__(self):
        super().__init__()
        self.estrategia_tipo_aceite = None # EstrategiaTipoAceite
        self.metodo_extraccion = None # <<MetodoExtraccion>>
        self.acidez = None # float
        self.cantidad_polifenoles = None # int
        self.color = None # str
        self.defectos_sensoriales = [] # List[DefectoSensorial]
        self.perfil_frutado = None # str
        self.nivel_frutado = None # NivelFrutado
        self.resistencia_termica = None # <<ResistenciaTermica>>
    
    # Setters
    def setEstrategiaTipoAceite(self, estrategia):
        self.estrategia_tipo_aceite = estrategia

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
    
    def setResistenciaTermica(self, resistencia):
        self.resistencia_termica = resistencia
    
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
    
    def getResistenciaTermica(self):
        return self.resistencia_termica

    def calcularPuntaje(self):
        self.puntaje = self.estrategia_tipo_aceite.calcularPuntaje(self)
        self.calcularCalidad()


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
    
    # Analizador
    def aceptarAnalizador(self, analizador):
        return analizador.analizarOliva(self)
    
    def calcularPuntaje(self):
        if self.uniformidad_color == UniformidadColor.ALTA:
            self.puntaje += 2
        elif self.uniformidad_color == UniformidadColor.MEDIA:
            self.puntaje += 1
        else:
            self.puntaje += 0
        
        if self.desvio_tamano < self.tamano_promedio/10:
            self.puntaje += 2
        elif self.desvio_tamano < self.tamano_promedio/20:
            self.puntaje += 1
        else:
            self.puntaje += 0
        
        if 5.5 < self.contenido_sal < 6.5:
            self.puntaje += 2
        elif 4.5 < self.contenido_sal < 7:
            self.puntaje += 1
        else:
            self.puntaje += 0
        
        if self.porcentaje_defectos_visuales < 5:
            self.puntaje += 2
        elif self.porcentaje_defectos_visuales < 15:
            self.puntaje += 1
        else:
            self.puntaje += 0
        
        if 3.9 < self.ph < 4.1:
            self.puntaje += 2
        elif 3.7 < self.ph < 4.3:
            self.puntaje += 1
        else:
            self.puntaje += 0
        
        self.calcularCalidad()