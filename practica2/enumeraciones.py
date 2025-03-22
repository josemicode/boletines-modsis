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