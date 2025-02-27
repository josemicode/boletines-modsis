from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Abono(ABC):
    def __init__(self, tipo, activo):
        self.tipo = tipo
        self.activo = activo
        
    @abstractmethod
    def calcularCoste(tiempo_uso):
        pass
    
    
class AbonoAnual(Abono):
    COSTO_ANUAL = 150
    LIMITE_TIEMPO = 30  # minutos
    COSTO_EXTRA = 2  # cada 5 minutos extra
    
    def __init__(self, fecha_inicio):
        super().__init__("Anual")
        self.fecha_inicio = fecha_inicio
        
    def calcularCoste(self, tiempo_uso):
        if not self.esValido():
            return float('inf')
        
        if tiempo_uso <= self.LIMITE_TIEMPO:
            return 0
        
        tiempo_extra = tiempo_uso - self.LIMITE_TIEMPO
        return (tiempo_extra // 5) * self.COSTO_EXTRA
    
    def esValido(self):
        fecha_expiracion = self.fecha_inicio + timedelta(days = 365)
        return datetime.now() < fecha_expiracion
    
    
class AbonoPrepago(Abono):
    COSTO_15_MINUTOS = 5
    
    def __init__(self, saldo):
        super().__init__("Prepago")
        self.saldo = saldo
    
    def calcularCoste(self, tiempo_uso):
        costo_total = (tiempo_uso // 15) * self.COSTO_15_MINUTOS
        self.saldo -= costo_total
        return costo_total
    
    def esValido(self):
        return self.saldo >= -5  
    
    
class AbonoTuristico(Abono):
    COSTO_BASE = 50
    LIMITE_TIEMPO = 120  # 2 horas
    COSTO_EXTRA = 10  # cada 15 minutos extra

    def __init__(self, fecha_inicio):
        super().__init__("Turístico")
        self.fecha_inicio = fecha_inicio
    
    def calcularCoste(self, tiempo_uso):
        if not self.esValido():
            return float('inf')  
        
        if tiempo_uso <= self.LIMITE_TIEMPO:
            return 0
        
        tiempo_extra = tiempo_uso - self.LIMITE_TIEMPO
        return (tiempo_extra // 15) * self.COSTO_EXTRA
    
    def esValido(self):
        fecha_expiracion = self.fecha_inicio + timedelta(days=7)
        return datetime.now() < fecha_expiracion
    
