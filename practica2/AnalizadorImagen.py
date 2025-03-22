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

    #Es una prueba, así a bote pronto es como habría que hacerlo no??
    #Tipo, lo que he hecho es copiar los ejemplos del enunciado
    '''
    Analizador de Madurez: analiza el estado de madurez de los frutos.
    o Para Aceite: Nivel de maduración (0-100), porcentaje de ácido oleico, índice de
    grasa.
     {"tipo_analisis": "madurez", "nivel_madurez":
    "integer (0-100)", "acido_oleico": "float (0.0-100.0)
    [%]", "indice_grasa": "float (0.0-100.0) [%]" }
    o Para Oliva de mesa: Nivel de maduración (verde, envero, negro), firmeza de la
    piel.
     {"tipo_analisis": "madurez", "estado_madurez":
    "string ('verde' | 'envero' | 'negro')",
    "firmeza_piel": "float (0.0-10.0) [N]" }
    '''
    #Sería tener estas clases, y luego en el Producto una clase abstracta, de aceptar o algo así, que redirija al analizador??
    #una cosa así +-
    '''
    class Aceite(Producto):
    def aceptarAnalizador(self, analizador):
        return analizador.analizarAceite(self)
    '''
    

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

#? Cuestion: es realmente necesario pasar el objeto aceite/oliva a los métodos de analizarAceite/analizarOliva? Si despues hace falta usarlo lo entiendo, pero si no, no seria mejor no pasar nada?



#Puede ser la vd, aunque voy a ponerlos todos, y si no simplemente es quitarlo rapido y fuera

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



class AnalizadorTamaño(AnalizadorImagen):
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
