from estados_lote_produccion import EnArmado

class LoteProduccion:
    def __init__(self, fecha_hora, num_lote):
        self.num_lote = num_lote
        self.lotes_materia_prima = [] # list[LoteMateriaPrima]
        self.productos_obtenidos = [] # list[Producto]
        self._estado = EnArmado(self, fecha_hora) # EstadoLoteProduccion
        self.historial_estados = [] # list[EstadoLoteProduccion]
        self.registrarEstado()
    
    # Getters
    def getNumLote(self):
        return self.num_lote

    def getLotesMateriaPrima(self):
        return self.lotes_materia_prima
    
    def getProductosObtenidos(self):
        return self.productos_obtenidos

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

        # print("pre-append")
        if self._estado.nuevoLoteMateriaPrima():
            # print("append")
            self.lotes_materia_prima.append(lote)
            return True

    def quitarLoteMateriaPrima(self, lote):
        if self._estado.quitarLoteMateriaPrima():
            self.lotes_materia_prima = list(filter(lambda aux: (aux != lote), self.lotes_materia_prima))
            lote.retroceder()

    def registrarProductos(self):
        if self._estado.registrarProductos():
            # print("bbb")
            for lote in self.lotes_materia_prima:
                # print("aaa")
                self.productos_obtenidos.append(lote.getProducto())
    
    #* Toma un GeneradorReporte y llama a su metodo generarReportes()
    #? En verdad, esto no le corresponde a LoteProduccion, sino a un controlador (sistema o main)
    # def generarReporte(self, generador_reporte):
    #     if self._estado.generarReporte():
    #         generador_reporte.generarReportes(self.lotes_materia_prima, self.productos_obtenidos)
    #     return False
    
    '''Entonces creamos una clase sistema que lo desarrolle?? Mira el diagrama que he hecho cambios y ves donde la podemos implementar'''