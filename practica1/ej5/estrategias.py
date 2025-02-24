from abc import ABC, abstractmethod
    # - Normal: implica que los usuarios podrán descargar el recurso
    # pagando el costo base del recurso.
    # - Oferta: se define una fecha límite y un porcentaje de descuento. Si
    # una compra se realiza antes de la fecha límite se aplica el
    # porcentaje de descuento, mientras que luego de dicha fecha se
    # cobra el costo base completo.
    # - Crowd-based: se define una cantidad de usuarios mínimos que
    # deben comprar el recurso. Solo cuando la cantidad de usuarios que
    # lo compran alcanza al menos ese límite, dichos compradores
    # podrán descargarlo, y se realizará el cobro considerando el precio
    # base del recurso.
class Estrategia(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calcularCoste(self, base):
        pass

    @abstractmethod
    def calcularPuntos(self, base):
        pass

    @abstractmethod
    def descargable(self, ventas):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Normal(Estrategia):
    def __init__(self):
        pass

    def calcularCoste(self, base):
        return base

    def calcularPuntos(self, base):
        return base * 10
    
    def descargable(self, ventas):
        return True
    
    def __str__(self):
        return "Normal"

class Oferta(Estrategia):
    def __init__(self, porcentaje, fecha_limite):
        self.porcentaje = porcentaje
        self.fecha_limite = fecha_limite

    def calcularCoste(self, base, fecha_actual):
        if fecha_actual < self.fecha_limite:
            return base * (1 - self.porcentaje)
        return base

    def calcularPuntos(self, base, fecha_actual):
        if fecha_actual < self.fecha_limite:
            return base * 5
        return base * 10
    
    def descargable(self, ventas):
        return True
    
    def __str__(self):
        return "Oferta"

class CrowdBased(Estrategia):
    def __init__(self, cupo_usuarios):
        self.minimo = cupo_usuarios

    def calcularCoste(self, base):
        return base

    def calcularPuntos(self, base):
        return base * (50 / self.minimo)
    
    def descargable(self, ventas):
        return ventas >= self.minimo
    
    def __str__(self):
        return "Crowd-based"