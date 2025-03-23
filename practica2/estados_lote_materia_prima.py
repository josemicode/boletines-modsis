from abc import ABC, abstractmethod
import datetime

class EstadoLoteMateriaPrima(ABC):
    def __init__(self, lote_materia_prima, fecha_hora):
        self._lote_materia_prima = lote_materia_prima
        self._fecha_hora = fecha_hora

    def getFechaHora(self):
        return self._fecha_hora

    #* Cambio de avance y retroceso a lista de detonantes específicos
    #? Motivo: escalabilidad
    # @abstractmethod
    # def avanzar(self):
    #     pass

    # @abstractmethod
    # def retroceder(self):
    #     pass

    @abstractmethod
    def finalizaRegistroImagenes(self):
        pass

    @abstractmethod
    def finalizaRegistroResultados(self):
        pass

    @abstractmethod
    def malaCalidadImagenes(self):
        pass

    @abstractmethod
    def registrarImagen(self, imagen):
        return False

    @abstractmethod
    def asignarResultado(self, resultado):
        return False

    @abstractmethod
    def asignarALoteProduccion(self, lote):
        pass

    @abstractmethod
    def infoBaseModificable(self):
        return False

class Ingresado(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def finalizaRegistroImagenes(self):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(EnAnalisis(self._lote_materia_prima, datetime.now()))

    def registrarImagen(self, imagen):
        return True

    def infoBaseModificable(self):
        return True

class EnAnalisis(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def finalizaRegistroResultados(self):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(Analizado(self._lote_materia_prima, datetime.now()))

    def malaCalidadImagenes(self):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(Ingresado(self._lote_materia_prima, datetime.now()))

    def asignarResultado(self, resultado):
        return True

class Analizado(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def asignarALoteProduccion(self, lote):
        lote.registrarLoteMateriaPrima(self._lote_materia_prima)
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(EnProduccion(self._lote_materia_prima, datetime.now()))

class EnProduccion(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def retroceder(self, _fecha_hora):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(Analizado(self._lote_materia_prima, _fecha_hora))