from abc import ABC, abstractmethod

class EstrategiaTipoAceite(ABC):
    @abstractmethod
    def calcularPuntaje(self, aceite):
        pass

class EstrategiaVirgenExtra(EstrategiaTipoAceite):
    def calcularPuntaje(self, aceite):
        pass

class EstrategiaVirgen(EstrategiaTipoAceite):
    def calcularPuntaje(self, aceite):
        pass

class EstrategiaDeOrujo(EstrategiaTipoAceite):
    def calcularPuntaje(self, aceite):
        pass