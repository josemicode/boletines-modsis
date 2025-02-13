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
    #* Finalmente, se esperaran objetos datetime como parametros; formatear en el main

    #? Otra pregunta de formato... hay que decidir si preferimos tipado fuerte o debil en la definicion
    #* Supongo que utilizaremos el debil, por simpleza en gran medida