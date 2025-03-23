from estados_lote_produccion import EnArmado

class LoteProduccion:
    def __init__(self, fecha_hora):
        self.lotes_materia_prima = [] # list[LoteMateriaPrima]
        self.productos_obtenidos = [] # list[Producto]
        self._estado = EnArmado(self, fecha_hora) # EstadoLoteProduccion
        self.historial_estados = [] # list[EstadoLoteProduccion]
        self.registrarEstado()
    
    # Getters
    def getLotesMateriaPrima(self):
        return self.lotes_materia_prima
    
    def getProductosObtenidos(self):
        return self.productos_obtenidos

    def nuevoLoteMateriaPrima(self, lote):
        self.lotes_materia_prima.append(lote)

    def nuevoProductoObtenido(self, producto):
        self.productos_obtenidos.append(producto)

    # Setters
    def setEstado(self, estado):
        self._estado = estado

    # State Methods
    def registrarEstado(self):
        self.historial_estados.append(self._estado)

    def finalizaArmado(self):
        self._estado.finalizaArmado()

    def finalizaProduccion(self):
        self._estado.finalizaProduccion()

    # Comprobar que el producto asignado al lote no sea diferente a los otros productos asignados a los lotes previamente asignados
    def nuevoLoteMateriaPrima(self, lote):
        if len(self.lotes_materia_prima) != 0:
            if(lote.getProducto() != self.lotes_materia_prima[0].getProducto()):
                return False

        if self._estado.nuevoLoteMateriaPrima():
            self.lotes_materia_prima.append(lote)
            return True

    def quitarLoteMateriaPrima(self, lote):
        if self._estado.quitarLoteMateriaPrima():
            self.lotes_materia_prima = list(filter(lambda aux: (aux != lote), self.lotes_materia_prima))

    def registrarProducto(self, producto):
        if self._estado.registrarProducto():
            self.productos_obtenidos.append(producto)