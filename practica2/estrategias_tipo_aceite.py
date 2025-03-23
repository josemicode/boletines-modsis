from abc import ABC, abstractmethod
from productos import Producto, Aceite
from enumeraciones import MetodoExtraccion, NivelFrutado, ResistenciaTermica

class EstrategiaTipoAceite(ABC):
    @abstractmethod
    def calcularPuntaje(self, aceite):
        pass

class EstrategiaVirgenExtra(EstrategiaTipoAceite):
    def calcularPuntaje(self, aceite):
        puntaje = 0

        if aceite.getAcidez() <= 0.3:
            puntaje += 2
        elif 0.4 <= aceite.getAcidez() <= 0.8:
            puntaje += 1
        else:
            puntaje += 0

        if aceite.getMetodoExtraccion() == MetodoExtraccion.PRENSADO:
            puntaje += 2
        elif aceite.getMetodoExtraccion() == MetodoExtraccion.CENTRIFUGADO:
            puntaje += 1
        else:
            puntaje += 0

        if aceite.getDefectosSensoriales() == []:
            puntaje += 2
        #? Si hay un defecto sensorial, pero es de gravedad baja, se le da un punto. He de decir que lo de menor a 2 me lo he inventado, pero pega
        elif len(aceite.getDefectosSensoriales()) == 1 and aceite.getDefectosSensoriales()[0].getGravedad() < 2:
            puntaje += 1
        else:
            puntaje += 0
        
        if aceite.getCantidadPolifenoles() >= 300:
            puntaje += 2
        elif 200 <= aceite.getCantidadPolifenoles() <= 299:
            puntaje += 1
        else:
            puntaje += 0
        
        if aceite.getNivelFrutado() == NivelFrutado.ALTO:
            puntaje += 2
        elif aceite.getNivelFrutado() == NivelFrutado.MEDIO:
            puntaje += 1
        else:
            puntaje += 0

        return puntaje

class EstrategiaVirgen(EstrategiaTipoAceite):
    def calcularPuntaje(self, aceite):
        puntaje = 0

        if aceite.getAcidez() <= 1:
            puntaje += 2
        elif 1.1 <= aceite.getAcidez() <= 2:
            puntaje += 1
        else:
            puntaje += 0
        
        if aceite.getMetodoExtraccion() == MetodoExtraccion.PRENSADO:
            puntaje += 2
        elif aceite.getMetodoExtraccion() == MetodoExtraccion.CENTRIFUGADO:
            puntaje += 1
        else:
            puntaje += 0

        if (aceite.getDefectosSensoriales() == []) or (len(aceite.getDefectosSensoriales()) == 1 and aceite.getDefectosSensoriales()[0].getGravedad() < 2):
            puntaje += 2
        elif len(aceite.getDefectosSensoriales()) == 2:
            puntaje += 1
        else:
            puntaje += 0
        
        if aceite.getCantidadPolifenoles() >= 200:
            puntaje += 2
        elif 100 <= aceite.getCantidadPolifenoles() <= 199:
            puntaje += 1
        else:
            puntaje += 0

        if (aceite.getNivelFrutado() == NivelFrutado.ALTO) or (aceite.getNivelFrutado() == NivelFrutado.MEDIO):
            puntaje += 2
        elif aceite.getNivelFrutado() == NivelFrutado.BAJO:
            puntaje += 1
        else:
            puntaje += 0

        return puntaje

class EstrategiaDeOrujo(EstrategiaTipoAceite):
    def calcularPuntaje(self, aceite):
        puntaje = 0

        if aceite.getAcidez() <= 0.3:
            puntaje += 2
        elif 0.4 <= aceite.getAcidez() <= 0.6:
            puntaje += 1
        else:
            puntaje += 0
    
        if aceite.getMetodoExtraccion() == MetodoExtraccion.REFINADO_ALTO:
            puntaje += 2
        elif aceite.getMetodoExtraccion() == MetodoExtraccion.REFINADO:
            puntaje += 1
        else:
            puntaje += 0
        
        if len(aceite.getDefectosSensoriales()) <= 2:
            puntaje += 2
        elif len(aceite.getDefectosSensoriales()) == 3:
            puntaje += 1
        else:
            puntaje += 0

        if aceite.getCantidadPolifenoles() >= 100:
            puntaje += 2
        elif 50 <= aceite.getCantidadPolifenoles() <= 99:
            puntaje += 1
        else:
            puntaje += 0
        
        if aceite.getResistenciaTermica() == ResistenciaTermica.ALTA:
            puntaje += 2
        elif aceite.getResistenciaTermica() == ResistenciaTermica.ESTABLE:
            puntaje += 1
        else:
            puntaje += 0

        return puntaje