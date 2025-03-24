from abc import ABC, abstractmethod
from datos_analisis import AnalisisImagen, DatoAnalisis

class AnalizadorImagen(ABC):
    def __init__(self, nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre

    @abstractmethod
    def analizarAceite(self, aceite):
        pass

    @abstractmethod
    def analizarOliva(self, oliva):
        pass

# Aclaracion: los metodos analizarAceite() y analizarOliva(), reciben los objetos aceite y oliva correspondiente a cada uno,
# en la implementacion actual no hace nada, tendría un uso en el caso de que esta funcionalidad tuviese una funcion real.

class AnalizadorMadurez(AnalizadorImagen):
    def __init__(self):
        super().__init__("Analizador de Madurez")

    def analizarAceite(self, aceite):
        d1 = DatoAnalisis("nivel_madurez", 85)
        d2 = DatoAnalisis("acido_oleico", 75.3)
        d3 = DatoAnalisis("indice_grasa", 18.2)
        return AnalisisImagen("madurez", [d1, d2, d3])


    def analizarOliva(self, oliva):
        d1 = DatoAnalisis("estado_madurez", "envero")
        d2 = DatoAnalisis("firmeza_piel", 6.5)
        return AnalisisImagen("madurez", [d1, d2])



class AnalizadorDefectos(AnalizadorImagen):
    def __init__(self):
        super().__init__("Analizador de Defectos")

    def analizarAceite(self, aceite):
        d1 = DatoAnalisis("hongos_detectados", True)
        d2 = DatoAnalisis("fermentacion_anomala", False)
        d3 = DatoAnalisis("danos_fisicos", "moderado")
        return AnalisisImagen("defectos", [d1, d2, d3])

    def analizarOliva(self, oliva):
        d1 = DatoAnalisis("golpes", 12)
        d2 = DatoAnalisis("arrugas", 8)
        d3 = DatoAnalisis("presencia_insectos", True)
        d4 = DatoAnalisis("pudricion", "leve")
        return AnalisisImagen("defectos", [d1, d2, d3, d4])




class AnalizadorHumedad(AnalizadorImagen):
    def __init__(self):
        super().__init__("Analizador de Humedad")

    def analizarAceite(self, aceite):
        d1 = DatoAnalisis("porcentaje_humedad", 42.7)
        return AnalisisImagen("humedad", [d1])

    def analizarOliva(self, oliva):
        d1 = DatoAnalisis("porcentaje_humedad", 37.5)
        d2 = DatoAnalisis("riesgo_moho", "medio")
        d3 = DatoAnalisis("idoneidad_conservacion", "buena")
        return AnalisisImagen("humedad", [d1, d2, d3])



class AnalizadorColor(AnalizadorImagen):
    def __init__(self):
        super().__init__("Analizador de Color")

    def analizarAceite(self, aceite):
        d1 = DatoAnalisis("color_preponderante", "verde oscuro")
        d2 = DatoAnalisis("indice_color_esperado", "verde-amarillo")
        d3 = DatoAnalisis("transparencia", "media")
        return AnalisisImagen("color", [d1, d2, d3])

    def analizarOliva(self, oliva):
        d1 = DatoAnalisis("clasificacion_color", {"verde claro": 40.0, "verde oscuro": 35.0, "negro": 25.0})
        d2 = DatoAnalisis("uniformidad_color", 85.0)
        return AnalisisImagen("color", [d1, d2])



class AnalizadorTamano(AnalizadorImagen):
    def __init__(self):
        super().__init__("Analizador de Tamaño")

    def analizarAceite(self, aceite):
        d1 = DatoAnalisis("tamano_promedio", 18.5) 
        d2 = DatoAnalisis("frutos_fuera_estandar", 12.3)  
        return AnalisisImagen("tamaño", [d1, d2])

    def analizarOliva(self, oliva):
        d1 = DatoAnalisis("clasificacion_calibre", "mediano")
        d2 = DatoAnalisis("frutos_fuera_estandar", 8.5) 
        return AnalisisImagen("tamaño", [d1, d2])
    
    
class AnalizadorVariedad(AnalizadorImagen):
    def __init__(self):
        super().__init__("Analizador de Variedad")

    def analizarAceite(self, aceite):
        variedades = [
            DatoAnalisis("variedad", "Picual"),
            DatoAnalisis("porcentaje", 55.0),
            DatoAnalisis("variedad", "Arbequina"),
            DatoAnalisis("porcentaje", 30.0),
            DatoAnalisis("variedad", "Hojiblanca"),
            DatoAnalisis("porcentaje", 15.0),
        ]
        return AnalisisImagen("variedades", variedades)

    def analizarOliva(self, oliva):
        variedades = [
            DatoAnalisis("variedad", "Manzanilla"),
            DatoAnalisis("porcentaje", 40.0),
            DatoAnalisis("variedad", "Gordal"),
            DatoAnalisis("porcentaje", 35.0),
            DatoAnalisis("variedad", "Sevillana"),
            DatoAnalisis("porcentaje", 25.0),
        ]
        return AnalisisImagen("variedades", variedades)
