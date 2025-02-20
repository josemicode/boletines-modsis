# Registrar un nuevo recurso: se indica el creador, una descripción del
# recurso, una imagen de previsualización, una URL de descarga, fecha de
# carga, su precio base y una estrategia de comercialización (que no podrán
# cambiar en el futuro)
class Recurso:
    def __init__(self, creador, descripcion, imagen, url, fecha, precio, estrategia):
        self.creador = creador
        self.descripcion = descripcion
        self.preview = imagen
        self.url_descarga = url
        self.fecha = fecha
        self.precio_base = precio
        self.estrategia = estrategia

    
    # def getCreador(self):
    #     return self.creador
    
    # def getDescripcion(self):
    #     return self.descripcion
    
    # def getPreview(self):
        # return self.preview
    