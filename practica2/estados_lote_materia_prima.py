from abc import ABC, abstractmethod

class EstadoLoteMateriaPrima(ABC):
    def __init__(self, lote_materia_prima, fecha_hora):
        self._lmp = lote_materia_prima
        self._fecha_hora = fecha_hora

    def getFechaHora(self):
        return self._fecha_hora

    @abstractmethod
    def avanzar(self):
        pass

    @abstractmethod
    def retroceder(self):
        pass

    @abstractmethod
    def registrarImagen(self, imagen):
        pass

    @abstractmethod
    def asignarResultado(self, resultado):
        pass

    @abstractmethod
    def asignarALoteProduccion(self, lote):
        pass

class Ingresado(EstadoLoteMateriaPrima):
    def avanzar(self, _fecha_hora):
        self._lmp.registrarEstado()
        self._lmp.setEstado(EnAnalisis(self._lmp, _fecha_hora))

    def registrarImagen(self, imagen):
        self._lmp._nuevaImagen(imagen)

    # Setter controllers

class EnAnalisis(EstadoLoteMateriaPrima):
    def avanzar(self, _fecha_hora):
        self._lmp.registrarEstado()
        self._lmp.setEstado(Analizado(self._lmp, _fecha_hora))

    def asignarResultado(self, resultado):
        self._lmp._nuevoResultado(resultado)

class Analizado(EstadoLoteMateriaPrima):
    def avanzar(self, _fecha_hora):
        self._lmp.registrarEstado()
        self._lmp.setEstado(EnProduccion(self._lmp, _fecha_hora))

    def asignarALoteProduccion(self, lote):
        #lote._nuevoLoteMateriaPrima(self._lmp)
        pass

class EnProduccion(EstadoLoteMateriaPrima):
    def retroceder(self, _fecha_hora):
        self._lmp.registrarEstado()
        self._lmp.setEstado(Analizado(self._lmp, _fecha_hora))