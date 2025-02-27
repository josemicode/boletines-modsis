class Sistema:
    def __init__(self):
        pass

    #...
    def recursoDescargablePor(self, recurso, usuario):
        if recurso not in usuario.getBiblioteca():
            return False
        
        if recurso.getEstrategia().descargable(recurso.getVentas()):
            usuario.nuevaUrl(recurso.getUrlDescarga())
            return True
        return False
