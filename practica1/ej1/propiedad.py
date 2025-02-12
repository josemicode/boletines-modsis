from datetime import datetime
from typing import List

class Propiedad:
    def __init__(self, identificador, coste_noche):
        self.id = identificador
        self.coste_noche = coste_noche
        self.reservada = False
    
    def precio(self):
        pass

    #? Handling de fechas...
    #? Opcion 1: crear un objeto separado (Si el profesor lo requiere)
    #? Opcion 2: utilizar la libreria datetime
    #* De ser la 2, hay dos maneras para introducir fechas (no muy importante, pero es un detalle):
    #* Introducir una fecha por tres parametros (dia, mes y anio) en el propio metodo y, en este, 
    #* formatearlo a objeto. La otra manera es que los metodos esperen el objeto datetime directamente, 
    #* dejando el formateo para la introduccion de datos del usuario (hipotetico main, que sabiendo
    #* que tenemos que demostrar funcionalidad no es tan hipotetico).

    #? Otra pregunta de formato... hay que decidir si preferimos tipado fuerte o debil en la definicion
    #? de metodos (Python permite ambas, es cuestion de conveniencia y complejidad)

    #* Este es uno fuerte:
    def funcionFuerte(self, valor: int, nombre: str, lista_decimales: List[float]) -> bool:
        return True
    
    #* Debil:
    def funcionDebil(self, valor, nombre, lista_decimales):
        return True
    
    #* La diferencia radica en si queremos que las funciones confien en que sabemos lo que hacemos 
    #* con los tipos de variables o no. El fuerte es mas pesado pero se autodocumenta.
