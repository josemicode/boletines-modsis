class Sistema:
    def __init__(self, lista_freelancers, lista_ofertas):
        self.freelancers = lista_freelancers
        self.ofertas = lista_ofertas

    def getFreelancersPorCategoria(self, categoria):
        lista = []
        for fl in self.freelancers:
            if categoria in fl.getCategorias():
                lista.append(fl)
        return lista
    
    def getOfertas(self):
        return self.ofertas

    def ordenarOfertasPorPuntaje(self):
        self.ofertas.sort(key=lambda oferta: oferta.getPuntaje(), reverse=True)