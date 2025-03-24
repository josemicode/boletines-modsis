from abc import ABC, abstractmethod
from datetime import datetime

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

    @abstractmethod
    def retroceder(self):
        pass

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
    def registrarImagen(self):
        pass

    @abstractmethod
    def asignarResultado(self):
        pass

    @abstractmethod
    def asignarALoteProduccion(self, lote):
        pass

    @abstractmethod
    def infoBaseModificable(self):
        pass

class Ingresado(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def finalizaRegistroImagenes(self):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(EnAnalisis(self._lote_materia_prima, datetime.now()))

    def finalizaRegistroResultados(self):
        pass

    def registrarImagen(self):
        return True

    def asignarResultado(self):
        return False

    def infoBaseModificable(self):
        return True

    def asignarALoteProduccion(self, lote):
        pass

    def malaCalidadImagenes(self):
        pass

    def retroceder(self):
        pass

class EnAnalisis(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def infoBaseModificable(self):
        return False

    def finalizaRegistroImagenes(self):
        pass

    def finalizaRegistroResultados(self):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(Analizado(self._lote_materia_prima, datetime.now()))

    def malaCalidadImagenes(self):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(Ingresado(self._lote_materia_prima, datetime.now()))

    def asignarALoteProduccion(self, lote):
        pass

    def asignarResultado(self):
        return True

    def registrarImagen(self):
        return False

    def retroceder(self):
        pass

class Analizado(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def infoBaseModificable(self):
        return False

    def finalizaRegistroImagenes(self):
        pass

    def finalizaRegistroResultados(self):
        pass

    def malaCalidadImagenes(self):
        pass

    def asignarALoteProduccion(self, lote):
        lote.nuevoLoteMateriaPrima(self._lote_materia_prima)
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(EnProduccion(self._lote_materia_prima, datetime.now()))

    def registrarImagen(self):
        return False

    def asignarResultado(self):
        return False

    def retroceder(self):
        pass

class EnProduccion(EstadoLoteMateriaPrima):
    def __init__(self, lote_materia_prima, fecha_hora):
        super().__init__(lote_materia_prima, fecha_hora)

    def infoBaseModificable(self):
        return False

    def finalizaRegistroImagenes(self):
        pass

    def finalizaRegistroResultados(self):
        pass

    def malaCalidadImagenes(self):
        pass

    def registrarImagen(self):
        return False

    def asignarALoteProduccion(self, lote):
        pass

    def asignarResultado(self):
        return False

    def retroceder(self):
        self._lote_materia_prima.registrarEstado()
        self._lote_materia_prima.setEstado(Analizado(self._lote_materia_prima, datetime.now()))