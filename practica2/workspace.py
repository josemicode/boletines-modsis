from productor import Productor
from lote_materia_prima import LoteMateriaPrima
from lote_produccion import LoteProduccion
from estados_lote_produccion import *
from productos import Producto, Oliva, Aceite
from imagen import Imagen
from analizadores_imagen import *
from generador_reportes import *
from enumeraciones import UniformidadColor, PerfilSabor, ProcesoCurado, MetodoExtraccion, NivelFrutado, ResistenciaTermica
from estrategias_tipo_aceite import *
from defecto_sensorial import DefectoSensorial
from datetime import date, datetime
#import uuid

def main():
    #* Productores
    productor1 = Productor("Juan", "Perez", "12345678A", "Calle Falsa 123", "123456789", "abc@gmail.com")
    productor2 = Productor("Pepe", "Lopez", "87654321B", "Calle La Verdad", "955678987", "pepe@pepe.com")

    #* Productos
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

    aceite1 = Aceite()
    aceite1.setLugarAlmacenaje("Granada Oeste")
    aceite1.setEstrategiaTipoAceite(EstrategiaVirgen())
    aceite1.setMetodoExtraccion(MetodoExtraccion.PRENSADO)
    aceite1.setAcidez(1.5)
    aceite1.setCantidadPolifenoles(170)
    aceite1.setColor("Verde oliva azulado")
    aceite1.nuevoDefectoSensorial(DefectoSensorial("Ligeramente soluble", 1))
    aceite1.setNivelFrutado(NivelFrutado.BAJO)
    aceite1.setResistenciaTermica(ResistenciaTermica.ESTABLE)

    #* Lotes Materia Prima
    lmp1 = LoteMateriaPrima(productor1, oliva1, date(2025, 1, 1), datetime.now())
    print("Codigo Lote Materia Prima 1:", lmp1.getCodigo())
    lmp2 = LoteMateriaPrima(productor2, aceite1, date(2024, 12, 12), datetime.now())
    print("Codigo Lote Materia Prima 2:", lmp2.getCodigo())

    #* Ingresado
    lmp1.setPesoBruto(120)
    lmp1.setPesoTara(100)
    img1 = Imagen("frontal_olivas.png")
    lmp1.registrarImagen(img1)
    lmp1.finalizaRegistroImagenes()

    lmp2.setPesoBruto(200)
    lmp2.setPesoTara(190)
    img2 = Imagen("primer_plano_botellas.jpeg")
    lmp2.registrarImagen(img2)
    lmp2.finalizaRegistroImagenes()

    #* En Analisis (Ciclo de vuelta a Ingresado para demostrar retroceso de estados)
    lmp1.malaCalidadImagenes()
    img3 = Imagen("lateral_olivas.png")
    lmp1.registrarImagen(img3)
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

    analizador_color = AnalizadorColor()
    analizador_humedad = AnalizadorHumedad()
    analisis4 = aceite1.aceptarAnalizador(analizador_color)
    analisis5 = aceite1.aceptarAnalizador(analizador_humedad)
    lmp2.registrarResultado(analisis4)
    lmp2.registrarResultado(analisis5)
    lmp2.finalizaRegistroResultados()

    #* Analizado --> Produccion
    #* Lotes de Produccion: En Armado
    lprod1 = LoteProduccion(datetime.now(), 100001)
    lmp1.asignarALoteProduccion(lprod1)
    # Comprobamos que se puede eliminar
    lprod1.quitarLoteMateriaPrima(lmp1)
    lmp1.asignarALoteProduccion(lprod1)
    lprod1.finalizaArmado()

    lprod2 = LoteProduccion(datetime.now(), 100002)
    lmp2.asignarALoteProduccion(lprod2)
    lprod2.finalizaArmado()

    #* Lotes de Produccion en Produccion
    lprod1.finalizaProduccion()
    lprod2.finalizaProduccion()

    #* Finalizado
    lprod1.registrarProductos()
    # print(len(lprod1.getProductosObtenidos()))
    oliva2 = lprod1.getProductosObtenidos()[0]
    oliva2.setCantidadProducida(60)
    oliva2.setUnidadCantidad("kg")
    oliva2.calcularPuntaje()
    print("Puntaje del Producto (Oliva): ", oliva2.getPuntaje())
    print("Calidad del Producto (Oliva): ", oliva2.getCalidad().value)

    lprod2.registrarProductos()
    aceite2 = lprod2.getProductosObtenidos()[0]
    aceite2.setCantidadProducida(110)
    aceite2.setUnidadCantidad("L")
    aceite2.calcularPuntaje()
    print("Puntaje del Producto (Aceite)", aceite2.getPuntaje())
    print("Calidad del Producto (Aceite)", aceite2.getCalidad().value)

    #* Generacion Reporte JSON
    generador1 = GeneradorReportesJSON()
    (reportes_materias_primas1, reportes_productos1) = generador1.generarReportes(lprod1)
    print(reportes_materias_primas1, "\n\n", reportes_productos1)

    (reportes_materias_primas2, reportes_productos2) = generador1.generarReportes(lprod2)
    print(reportes_materias_primas2, "\n\n", reportes_productos2)

if __name__ == "__main__":
    main()