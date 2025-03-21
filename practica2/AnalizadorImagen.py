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

    # def analizarAceite(self, aceite):
    #     return {
    #         "tipo_analisis": "madurez",
    #         "nivel_madurez": 85,  
    #         "acido_oleico": 75.3,
    #         "indice_grasa": 18.2
    #     }

    def analizarAceite(self, aceite):
        d1 = DatoAnalisis("nivel_madurez", 85)
        d2 = DatoAnalisis("acido_oleico", 75.3)
        d3 = DatoAnalisis("indice_grasa", 18.2)
        return AnalisisImagen("madurez", [d1, d2, d3])

    # def analizarOliva(self, oliva):
    #     return {
    #         "tipo_analisis": "madurez",
    #         "estado_madurez": "envero",
    #         "firmeza_piel": 6.5
    #     }

    def analizarOliva(self, oliva):
        d1 = DatoAnalisis("estado_madurez", "envero")
        d2 = DatoAnalisis("firmeza_piel", 6.5)
        return AnalisisImagen("madurez", [d1, d2])

#? Cuestion: es realmente necesario pasar el objeto aceite/oliva a los métodos de analizarAceite/analizarOliva? Si despues hace falta usarlo lo entiendo, pero si no, no seria mejor no pasar nada?