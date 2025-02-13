from abc import ABC, abstractmethod
from datetime import date

'''
Se espera una estructura que permita la futura implementacion de reglas, 
asumiremos una genérica en la cual exista un argumento que simule el factor 
de aumento/reduccion en valor absoluto (no porcentual) y de signo relevante
'''

class Regla(ABC):
    @abstractmethod
    def __init__(self, factor):
        self.factor = factor
    
    @property
    @abstractmethod
    def prioridad(self):
        pass

    @abstractmethod
    def aplicar(self, reserva_inicio, reserva_fin):
        pass

class ReglaRango(Regla):
    def __init__(self, factor, fecha_inicio, fecha_fin):
        super.__init__(factor)
        self.inicio = fecha_inicio
        self.fin = fecha_fin
        self.prioridad = 1

    @property
    def prioridad(self):
        return self.prioridad
    
    def diasCompartidos(self, entrada, salida):
        menor = max(entrada, self.inicio)
        mayor = min(salida, self.fin)

        if menor > mayor:
            return 0;

        #! Dependiendo de como se calcule (diferencia entre un dia y el mismo = 1 // 0)
        return (mayor - menor).days

    def aplicar(self, reserva_inicio, reserva_fin, precio):
        dias = self.diasCompartidos(reserva_inicio, reserva_fin)
        return dias * precio * self.factor

class ReglaProlongacion(Regla):
    def __init__(self, factor, dias_bonus):
        super.__init__(factor)
        self.dias_bonus = dias_bonus
        self.prioridad = 2

    @property
    def prioridad(self):
        return self.prioridad
    
    def aplicar(self, reserva_inicio, reserva_fin, precio):
        dias = (reserva_fin - reserva_inicio).days
        if dias < self.dias_bonus:
            return 0
        
        return dias * precio * self.factor
    
    '''
    2x + 2xp -> x + p, 3x + xp -> x(3 + p)
    4x - 2p  -> 2x - p, 4x + p
    '''