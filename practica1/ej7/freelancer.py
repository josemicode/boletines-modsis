# Registrar un freelancer: Se le indica el nombre del freelancer, su dirección
# de email, el precio de hora de trabajo, y las categorías (ej.: Desarrollo
# Web, Diseño Gráfico, etc.).
class Freelancer:
    def __init__(self, nombre, email, precio_hora, lista_categorias):
        self.nombre = nombre
        self.email = email
        self.precio_hora = precio_hora
        self.categorias = lista_categorias # lista de categorias (enums)
        self.puntaje = 0

    def getNombre(self):
        return self.nombre
    
    def getEmail(self):
        return self.email
    
    def getPrecioHora(self):
        return self.precio_hora
    
    def getCategorias(self):
        return self.categorias
    
    def sumarPuntaje(self, puntaje):
        self.puntaje += puntaje
    
    def __str__(self):
        return f"Freelancer: nombre - {self.nombre}, email - {self.email}, precio por hora - {self.precio_hora}"