from abc import ABC, abstractmethod
import datetime

class EstadoLoteProduccion(ABC):
    def __init__(self, lote_produccion, fecha_hora):
        self._lote_produccion = lote_produccion
        self._fecha_hora = fecha_hora
    
    def getFechaHora(self):
        return self._fecha_hora
    
    @abstractmethod
    def finalizaArmado(self):
        pass

    @abstractmethod
    def finalizaProduccion(self):
        pass

    @abstractmethod
    def quitarLoteMateriaPrima(self):
        return False

    @abstractmethod
    def nuevoLoteMateriaPrima(self):
        return False

    @abstractmethod
    def registrarProducto(self):
        return False

    # @abstractmethod
    # def generarReporte(self):
    #     return False

class EnArmado(EstadoLoteProduccion):
    def __init__(self, lote_produccion, fecha_hora):
        super().__init__(lote_produccion, fecha_hora)
    
    def quitarLoteMateriaPrima(self):
        return True
    
    def nuevoLoteMateriaPrima(self):
        True
    
    def finalizaArmado(self):
        self._lote_produccion.registrarEstado()
        self._lote_produccion.setEstado(EnProduccion(self._lote_produccion, datetime.now()))

class EnProduccion(EstadoLoteProduccion):
    def __init__(self, lote_produccion, fecha_hora):
        super().__init__(lote_produccion, fecha_hora)

    def finalizaProduccion(self):
        self._lote_produccion.registrarEstado()
        self._lote_produccion.setEstado(Finalizado(self._lote_produccion, datetime.now()))

class Finalizado(EstadoLoteProduccion):
    def __init__(self, lote_produccion, fecha_hora):
        super().__init__(lote_produccion, fecha_hora)

    def registrarProducto(self):
        return True
    
    # def generarReporte(self):
    #     return True