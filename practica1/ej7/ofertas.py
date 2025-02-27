from abc import ABC, abstractmethod
from datetime import date
#from dateutil.relativedelta import relativedelta
# Registrar oferta para proyecto: para brindarle flexibilidad a cada freelancer
# a la hora de cotizar los proyectos según aspectos profesionales no
# contemplados en la aplicación, las ofertas de trabajo pueden ser:
#     - por hora de trabajo: Una oferta por hora de trabajo implica que el
#     freelancer cotiza el proyecto en función de las horas especificadas
#     en su oferta y su propio precio por hora de trabajo. Se requiere
#     saber la fecha de la oferta, la cantidad de horas estimadas y la
#     fecha de entrega estimada.
#     - por posición de trabajo: Una oferta por posición implica que el
#     freelancer cotiza el proyecto en función de cobrar un sueldo
#     mensual por una cantidad de horas de trabajo por mes por una
#     cantidad de meses determinada.
class Oferta(ABC):
    @abstractmethod
    def __init__(self, freelancer):
        self.freelancer = freelancer

    @abstractmethod
    def getFreelancer(self):
        pass

    @abstractmethod
    def calcularPrecioFinal(self):
        pass

    @abstractmethod
    def getPuntaje(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class OfertaPorHora(Oferta):
    def __init__(self, freelancer, horas, fecha_oferta, fecha_entrega):
        super().__init__(freelancer)
        self.fecha_oferta = fecha_oferta
        self.horas = horas
        self.fecha_entrega = fecha_entrega
        self.puntaje = 0

    def getFreelancer(self):
        return self.freelancer

    def getFechaEntrega(self):
        return self.fecha_entrega

    def calcularPrecioFinal(self):
        return self.horas * self.freelancer.getPrecioHora()

    def getPuntaje(self):
        self.puntaje = self.calcularPrecioFinal() // (self.fecha_entrega - self.fecha_oferta).days
        return self.puntaje

    def __str__(self):
        return f"Oferta por hora: {self.horas} horas a {self.freelancer.getPrecioHora()} por hora, puntaje: {self.puntaje}"

class OfertaPorPosicion(Oferta):
    def __init__(self, freelancer, horas_por_mes, salario, meses, fecha_oferta):
        super().__init__(freelancer)
        self.horas = horas_por_mes
        self.salario = salario
        self.meses = meses
        self.fecha_oferta = fecha_oferta
        self.fecha_entrega = None
        self.puntaje = 0

    def getFreelancer(self):
        return self.freelancer

    def calcularPrecioFinal(self):
        return self.salario * self.meses
    
    def calcularFechaEntrega(self):
        meses = self.fecha_oferta.month + self.meses
        anio = meses % 12
        if anio > 0:
            meses = meses // 12
        self.fecha_entrega = date(self.fecha_oferta.year + anio, self.fecha_oferta.month + meses, self.fecha_oferta.day)
    
    def getFechaEntrega(self):
        return self.fecha_entrega
    
    #* calcular fecha de entrega en base a cuantos meses pasa desde la fecha de inicio
    def getPuntaje(self):
        self.calcularFechaEntrega()
        #fecha_entrega = self.fecha_oferta + relativedelta(days=self.meses)
        self.puntaje = self.calcularPrecioFinal() // (self.fecha_entrega - self.fecha_oferta).days
        return self.puntaje
    
    def __str__(self):
        return f"Oferta por posición: {self.salario} por mes por {self.horas} horas por {self.meses} meses, puntaje: {self.puntaje}"

'''
[] --- []
        |
[] --- []
 L []
'''