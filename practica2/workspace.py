from productor import Productor
from lote_materia_prima import LoteMateriaPrima
from lote_produccion import LoteProduccion
from estados_lote_produccion import *
from productos import Producto, Oliva, Aceite
from imagen import Imagen
from analizadores_imagen import *
from generador_reportes import *
from enumeraciones import UniformidadColor, PerfilSabor, ProcesoCurado, Calidad
from datetime import date, datetime
#import uuid

def main():
    #* Productor
    productor1 = Productor("Juan", "Perez", "12345678A", "Calle Falsa 123", "123456789", "abc@gmail.com")

    #* Producto
    oliva1 = Oliva()
    oliva1.setLugarAlmacenaje("Ecija")
    oliva1.setUniformidadColor(UniformidadColor.MEDIA)
    oliva1.setTamanoPromedio(33.3)
    oliva1.setDesvioTamano(2)
    oliva1.setPerfilSabor(PerfilSabor.ACIDO)
    oliva1.setProcesoCurado(ProcesoCurado.SALMUERA)
    oliva1.setContenidoSal(5.6)
    oliva1.setPorcentajeDefectosVisuales(1.2)
    oliva1.setPh(4)

    #* Lote Materia Prima
    lmp1 = LoteMateriaPrima(productor1, oliva1, date(2025, 1, 1), datetime.now())
    print("Codigo Lote Materia Prima:", lmp1.getCodigo())

    #* Ingresado
    lmp1.setPesoBruto(120)
    lmp1.setPesoTara(100)
    img1 = Imagen("frontal_olivas.png")
    lmp1.registrarImagen(img1)
    lmp1.finalizaRegistroImagenes()

    #* En Analisis
    lmp1.malaCalidadImagenes()
    img2 = Imagen("lateral_olivas.png")
    lmp1.registrarImagen(img2)
    lmp1.finalizaRegistroImagenes()

    analizador_variedad = AnalizadorVariedad()
    analizador_tamano = AnalizadorTamano()
    analizador_madurez = AnalizadorMadurez()
    analisis1 = oliva1.aceptarAnalizador(analizador_variedad)
    analisis2 = oliva1.aceptarAnalizador(analizador_tamano)
    analisis3 = oliva1.aceptarAnalizador(analizador_madurez)
    lmp1.registrarResultado(analisis1)
    lmp1.registrarResultado(analisis2)
    lmp1.registrarResultado(analisis3)
    lmp1.finalizaRegistroResultados()

    #* Analizado
    #* Lote de Produccion
    lprod1 = LoteProduccion(datetime.now(), 100001)
    lmp1.asignarALoteProduccion(lprod1)
    lprod1.quitarLoteMateriaPrima(lmp1)
    lmp1.asignarALoteProduccion(lprod1)

    # if isinstance(lprod1._estado, EnArmado):
    #     print("-----")

    #* En Produccion, En Armado
    lprod1.finalizaArmado()

    #* Lote de Produccion en Produccion
    lprod1.finalizaProduccion()

    #* Finalizado
    lprod1.registrarProductos()
    # print(len(lprod1.getProductosObtenidos()))
    oliva2 = lprod1.getProductosObtenidos()[0]
    oliva2.setCantidadProducida(60)
    oliva2.setUnidadCantidad("kg")
    oliva2.calcularPuntaje()
    print("Puntaje del Producto: ", oliva2.getPuntaje())
    print("Calidad del Producto: ", oliva2.getCalidad().value)

    #* Generacion Reporte JSON
    generador1 = GeneradorReportesJSON()
    (reportes_materias_primas, reportes_productos) = generador1.generarReportes(lprod1)
    print(reportes_materias_primas, "\n\n", reportes_productos)

if __name__ == "__main__":
    main()