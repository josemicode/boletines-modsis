from abc import ABC, abstractmethod

class Regla(ABC):
    @property
    @abstractmethod
    def prioridad(self):
        pass

class ReglaRango(Regla):
    def __init__(self):
        self.prioridad = 1

    @property
    def prioridad(self):
        return self.prioridad

class ReglaProlongacion(Regla):
    def __init__(self):
        self.prioridad = 2

    @property
    def prioridad(self):
        return self.prioridad