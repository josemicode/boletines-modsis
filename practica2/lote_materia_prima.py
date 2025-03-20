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
        self._codigo = self.codegen()
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
    def _nuevaImagen(self, imagen):
        self.imagenes.append(imagen)

    def _nuevoResultado(self, resultado):
        self.resultados.append(resultado)

    def registrarEstado(self):
        self.historial_estados.append(self._estado)

    # Code gen
    def codegen(self):
        for i in range(24):
            res += str(random.randint(0, 9))
        return res

    # State Methods
    def setEstado(self, estado):
        self._estado = estado

    def avanzar(self, fecha_hora):
        self._estado.avanzar(fecha_hora)

    def retroceder(self, fecha_hora):
        self._estado.retroceder(fecha_hora)

    def registrarImagen(self, imagen):
        self._estado.registrarImagen(imagen)

    def registrarResultado(self, resultado):
        self._estado.asignarResultado(resultado)