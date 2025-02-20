# Registrar un freelancer: Se le indica el nombre del freelancer, su dirección
# de email, el precio de hora de trabajo, y las categorías (ej.: Desarrollo
# Web, Diseño Gráfico, etc.).
class Freelancer:
    def __init__(self, nombre, email, precio_hora, categoria):
        self.nombre = nombre
        self.email = email
        self.precio_hora = precio_hora
        self.categoria = categoria #? Deberia ser una lista de categorias? Esta en plural...