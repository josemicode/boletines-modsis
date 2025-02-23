from abc import ABC, abstractmethod
from datetime import date
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
    def __init__(self):
        pass

    @abstractmethod
    def calcularPrecioFinal(self):
        pass

    @abstractmethod
    def getPuntaje(self):
        pass

class OfertaPorHora(Oferta):
    def __init__(self, fecha_oferta, horas, fecha_entrega, precio_hora):
        self.fecha_oferta = fecha_oferta
        self.horas = horas
        self.precio_hora = precio_hora
        self.fecha_entrega = fecha_entrega

    def calcularPrecioFinal(self):
        return self.horas * self.precio_hora

    def getPuntaje(self):
        return self.calcularPrecioFinal() / (self.fecha_entrega - self.fecha_oferta).days

class OfertaPorPosicion(Oferta):
    def __init__(self, fecha_oferta, salario, horas_por_mes, meses):
        self.fecha_oferta = fecha_oferta
        self.salario = salario
        self.horas = horas_por_mes
        self.meses = meses

    def calcularPrecioFinal(self):
        return self.salario * self.meses
    
    #* calcular fecha de entrega en base a cuantos meses pasa desde la fecha de inicio
    def getPuntaje(self):
        fecha_entrega = date(self.fecha_oferta.year, self.fecha_oferta.month + self.meses, self.fecha_oferta.day)
        return self.calcularPrecioFinal() / (fecha_entrega - self.fecha_oferta).days