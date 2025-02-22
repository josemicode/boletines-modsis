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
        self.ventas = 0

    
    def getCreador(self):
        return self.creador
    
    def getDescripcion(self):
        return self.descripcion
    
    def getPreview(self):
        return self.preview
    
    def getUrlDescarga(self):
        return self.url_descarga
    
    def getFecha(self):
        return self.fecha
    
    def getPrecioBase(self):
        return self.precio_base
    
    def getEstrategia(self):
        return self.estrategia
    
    def getVentas(self):
        return self.ventas
    
    def vender(self):
        self.ventas += 1