from abc import ABC, abstractmethod

class GeneradorReportes(ABC):
    #* Template Method
    def generarReportes(self, lista_materias_primas, lista_productos):
        lista_reportes_materias_primas = []
        lista_reportes_productos = []

        for materia_prima in lista_materias_primas:
            aux = self.generarReporteMateriaPrima(materia_prima)
            lista_reportes_materias_primas.append(aux)

        for producto in lista_productos:
            aux = self.generarReporteProducto(producto)
            lista_reportes_productos.append(aux)

        return (lista_reportes_materias_primas, lista_reportes_productos)
    
    @abstractmethod
    def generarReporteMateriaPrima(self, materia_prima):
        pass

    @abstractmethod
    def generarReporteProducto(self, producto):
        pass

class GeneradorReportesPDF(GeneradorReportes):
    def generarReporteMateriaPrima(self, materia_prima):
    # Los lotes de materia prima incluidos en el lote de producción (indicando número de lote, productor, fecha de cosecha, fecha y hora de ingreso a planta, y peso neto)
        return f"Reporte de materia prima:\n - Lote de produccion: {materia_prima.getNumLote()}\n - Productor: {materia_prima.getProductor().toString()}\n - Fecha de cosecha: {materia_prima.getFechaCosecha()}\n - Fecha y hora de ingreso a planta: {materia_prima.getLlegadaPlanta()}\n - Peso neto: {materia_prima.getPesoTara()}"

    def generarReporteProducto(self, producto):
    # El/los productos obtenidos del proceso de producción, indicando:
    # - Número de seguimiento interno
    # - Cantidad producida (cantidad y unidad)
    # - Lugar de almacenaje (que incluye número de galpón y número de sala)
    # - Calidad (ALTA, MEDIA, BAJA)
        return f"Reporte de producto:\n - Numero de seguimiento interno: {producto.getCodigo()}\n - Cantidad producida: {producto.getCantidadProducida()} {producto.getUnidadCantidad()}\n - Lugar de almacenaje: {producto.getLugarAlmacenaje()}\n - Calidad: {producto.getCalidad()}"