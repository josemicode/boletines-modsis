from enum import Enum

#* Enum para metodos de extraccion de aceite
class MetodoExtraccion(Enum):
    PRENSADO = "Prensado En Frio"
    CENTRIFUGADO = "Centrifugado"
    REFINADO = "Refinado"
    DISOLVENTE = "Con Disolvente"

class NivelFrutado(Enum):
    ALTO = "Nivel Frutado Alto"
    MEDIO = "Nivel Frutado Medio"
    BAJO = "Nivel Frutado Bajo"

class UniformidadColor(Enum):
    ALTO = "Uniformidad de Color Alta"
    MEDIO = "Uniformidad de Color Media"
    BAJO = "Uniformidad de Color Baja"

class PerfilSabor(Enum):
    AMARGO = "Perfil de Sabor Amargo"
    SALADO = "Perfil de Sabor Salado"
    ACIDO = "Perfil de Sabor Acido"

class ProcessoCurado(Enum):
    NATURAL = "Proceso de Curado Natural"
    SALMUERA = "Proceso de Curado en Salmuera"
    SOSA = "Proceso de Curado en Sosa Caustica"
    FERMETACION = "Proceso de Curado por Fermentacion"

class Calidad(Enum):
    ALTA = "Calidad Alta"
    MEDIA = "Calidad Media"
    BAJA = "Calidad Baja"