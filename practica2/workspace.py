from productor import Productor
from lote_materia_prima import LoteMateriaPrima
from productos import Producto, Oliva, Aceite
from imagen import Imagen
from analizadores_imagen import *
from enumeraciones import UniformidadColor, PerfilSabor, ProcesoCurado
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

if __name__ == "__main__":
    main()