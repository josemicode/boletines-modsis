from enum import Enum

#* Enum para metodos de extraccion de aceite
class MetodoExtraccion(Enum):
    PRENSADO = "Prensado En Frio"
    CENTRIFUGADO = "Centrifugado"
    REFINADO = "Refinado"
    REFINADO_ALTO = "Refinado Alta Calidad"
    DISOLVENTE = "Con Disolvente"

class ResistenciaTermica(Enum):
    ALTA = "Muy Estable en Frituras"
    ESTABLE = "Estable"
    NINGUNA = "Inestable"

class NivelFrutado(Enum):
    ALTO = "Nivel Frutado Alto"
    MEDIO = "Nivel Frutado Medio"
    BAJO = "Nivel Frutado Bajo"
    NADA = "Sin Nivel Frutado"

class UniformidadColor(Enum):
    ALTA = "Uniformidad de Color Alta"
    MEDIA = "Uniformidad de Color Media"
    BAJA = "Uniformidad de Color Baja"

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