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
    
    @abstractmethod
    def getPrioridad(self):
        pass

    @abstractmethod
    def aplicar(self, reserva_inicio, reserva_fin, precio_noche, precio_total):
        pass

class ReglaRango(Regla):
    prioridad = 1
    def __init__(self, factor, fecha_inicio, fecha_fin):
        super().__init__(factor)
        self.inicio = fecha_inicio
        self.fin = fecha_fin
    
    def getPrioridad(self):
        #print(self.prioridad, " -<")
        return ReglaRango.prioridad
    
    def diasCompartidos(self, entrada, salida):
        menor = max(entrada, self.inicio)
        mayor = min(salida, self.fin)

        if menor > mayor:
            return 0

        return (mayor - menor).days

    def aplicar(self, reserva_inicio, reserva_fin, precio_noche, precio_total):
        dias = self.diasCompartidos(reserva_inicio, reserva_fin)
        return precio_total + (dias * precio_noche * self.factor)

class ReglaProlongacion(Regla):
    prioridad = 2 
    def __init__(self, factor, dias_bonus):
        super().__init__(factor)
        self.dias_bonus = dias_bonus

    def getPrioridad(self):
        #print(ReglaProlongacion.prioridad, " -<")
        return ReglaProlongacion.prioridad
    
    def aplicar(self, reserva_inicio, reserva_fin, precio_noche, precio_total):
        dias = (reserva_fin - reserva_inicio).days
        if dias < self.dias_bonus:
            return 0
        
        return precio_total + (precio_total * self.factor)
    
    '''
    2x + 2xp -> x + p, 3x + xp -> x(3 + p)
    4x - 2p  -> 2x - p, 4x + p
    '''