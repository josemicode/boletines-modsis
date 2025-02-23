# Registrar un proyectista: Se le indica el nombre del proyectista y su
# dirección de email.
class Proyectista:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        proyectos = []

    def getNombre(self):
        return self.nombre
    
    def getEmail(self):
        return self.email
    
    def getProyectosPorCategoria(self, categoria):
        lista = []
        for pr in self.proyectos:
            if pr.getCategoria() == categoria:
                lista.append(pr)
        return lista