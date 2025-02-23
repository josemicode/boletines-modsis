from abc import ABC, abstractmethod
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

class OfertaPorHora(Oferta):
    def __init__(self, fecha_oferta, horas, fecha_entrega):
        self.fecha_oferta = fecha_oferta
        self.horas = horas
        self.fecha_entrega = fecha_entrega

class OfertaPorPosicion(Oferta):
    def __init__(self, fecha_oferta, salario, horas_por_mes, meses):
        self.salario = salario
        self.horas = horas_por_mes
        self.meses = meses