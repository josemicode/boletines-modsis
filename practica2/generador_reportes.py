from abc import ABC, abstractmethod
import json

class GeneradorReportes(ABC):
    #* Template Method
    def generarReportes(self, lote_produccion):
        lista_materias_primas = lote_produccion.getLotesMateriaPrima()
        lista_productos = lote_produccion.getProductosObtenidos()

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

class GeneradorReportesJSON(GeneradorReportes):
    def generarReporteMateriaPrima(self, materia_prima):
        datos_materia_prima = {}
        datos_materia_prima["lote_produccion"] = materia_prima.getNumLote()
        datos_materia_prima["productor"] = materia_prima.getProductor().toString()
        datos_materia_prima["fecha_cosecha"] = materia_prima.getFechaCosecha()
        datos_materia_prima["fecha_ingreso_planta"] = materia_prima.getLlegadaPlanta()
        datos_materia_prima["peso_neto"] = materia_prima.getPesoTara()
        with open("reporte_materia_prima.json", "w", encoding="utf-8") as f:
            json.dump(datos_materia_prima, f, indent=4, ensure_ascii=False)
    
    def generarReporteProducto(self, producto):
        datos_producto = {}
        datos_producto["codigo"] = producto.getCodigo()
        datos_producto["cantidad_producida"] = producto.getCantidadProducida()
        datos_producto["unidad_cantidad"] = producto.getUnidadCantidad()
        datos_producto["lugar_almacenaje"] = producto.getLugarAlmacenaje()
        datos_producto["calidad"] = producto.getCalidad()
        with open("reporte_producto.json", "w", encoding="utf-8") as f:
            json.dump(datos_producto, f, indent=4, ensure_ascii=False)