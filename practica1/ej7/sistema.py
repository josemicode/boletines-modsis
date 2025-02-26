class Sistema:
    def __init__(self, lista_freelancers):
        self.freelancers = lista_freelancers
        # self.ofertas = lista_ofertas #! quitar

    def getFreelancersPorCategoria(self, categoria):
        lista = []
        for fl in self.freelancers:
            if categoria in fl.getCategorias():
                lista.append(fl)
        return lista
    
    #! DL Proyecto
    # def getOfertas(self):
    #     return self.ofertas

    #! Delegar a Proyecto
    # def ordenarOfertasPorPuntaje(self):
    #     self.ofertas.sort(key=lambda oferta: oferta.getPuntaje(), reverse=True)