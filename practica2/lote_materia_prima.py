from estados_lote_materia_prima import Ingresado
import random

class LoteMateriaPrima:
    # productor: Productor
    # fecha_cosecha: date
    # llegada_planta: datetime
    def __init__(self, productor, fecha_cosecha, llegada_planta):
        self._productor = productor
        self._fecha_cosecha = fecha_cosecha
        self._llegada_planta = llegada_planta
        self._codigo = self._codeGen()
        self._peso_bruto = None
        self._peso_tara = None
        #self._producto = None
        self.imagenes = []
        self.resultados = []
        self.historial_estados = []
        self._estado = Ingresado(self, llegada_planta)
        self.registrarEstado()

    # Getters
    def getProductor(self):
        return self._productor

    def getFechaCosecha(self):
        return self._fecha_cosecha

    def getLlegadaPlanta(self):
        return self._llegada_planta

    def getCodigo(self):
        return self._codigo

    # Setters
    def setPesoBruto(self, peso_bruto):
        if self._estado.infoBaseModificable():
            self._peso_bruto = peso_bruto

    def setPesoTara(self, peso_tara):
        if self._estado.infoBaseModificable():
            self._peso_tara = peso_tara

    def registrarEstado(self):
        self.historial_estados.append(self._estado)

    # Code generation
    def _codeGen(self):
        for i in range(24):
            res += str(random.randint(0, 9))
        return res

    # State Methods
    def setEstado(self, estado):
        self._estado = estado

    def finalizaRegistroImagenes(self):
        self._estado.finalizaRegistroImagenes()

    def finalizaRegistroResultados(self):
        self._estado.finalizaRegistroResultados()

    def malaCalidadImagenes(self):
        self._estado.malaCalidadImagenes()

    def asignarALoteProduccion(self, lote_produccion):
        self._estado.asignarALoteProduccion(lote_produccion)

    def registrarImagen(self, imagen):
        if self._estado.registrarImagen(imagen):
            self.imagenes.append(imagen)

    def registrarResultado(self, resultado):
        if self._estado.asignarResultado(resultado):
            self.resultados.append(resultado)