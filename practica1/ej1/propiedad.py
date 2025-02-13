from datetime import datetime
#import reglas
class Propiedad:
    def __init__(self, identificador, coste_noche):
        self.id = identificador
        self.coste_noche = coste_noche
        self.reglas = []
        #TODO: self.reservas = []
    
    def nuevaRegla(self, regla):
        self.reglas.append(regla)
        self.reglas.sort(key=lambda r: r.prioridad)
    
    def precio(self, fecha_inicio, fecha_fin):
        precio = (fecha_fin - fecha_inicio).days * self.coste_noche
        for regla in self.reglas:
            precio += regla.aplicar()
        return precio
    
    #TODO: handling de reservas
    #* Deberia buscar coincidencias en el rango de dias introducido con los de los registros
    #* Puede devolver un bool para confirmar
    def reserva(self):
        pass

    #? Handling de fechas...
    #* Finalmente, se esperaran objetos datetime como parametros; formatear en el main

    #? Otra pregunta de formato... hay que decidir si preferimos tipado fuerte o debil en la definicion
    #* Supongo que utilizaremos el debil, por simpleza en gran medida