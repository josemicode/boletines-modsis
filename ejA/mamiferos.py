class Mamifero:
    def __init__(self, id, especie, fecha_nacimiento):
        self.id = id
        self.raza = especie
        self.fecha_nacimiento = fecha_nacimiento
    
    def identificador(self, unIdentificador):
        self.id = unIdentificador
    
    def identificador(self):
        return self.id
    
    def especie(self, unaEspecie):
        self.raza = unaEspecie
    
    def especie(self):
        return self.raza
    
    def fechaDeNacimiento(self, fecha):
        self.fecha_nacimiento = fecha
    
    def fechaDeNacimiento(self):
        return self.fecha_nacimiento
    
    def padre(self, elPadre):
        self.papa = elPadre
    
    def padre(self):
        return self.papa
    
    def madre(self, laMadre):
        self.mama = laMadre
    
    def abueloMaterno(self):
        # Revisar en un futuro si hace falta comprobar doblemente
        mama_aux = self.madre()
        if mama_aux != None:
            return mama_aux.padre()
    
    def abuelaMaterna(self):
        mama_aux = self.madre()
        if mama_aux != None:
            return mama_aux.madre()
    
    def abueloPaterno(self):
        papa_aux = self.padre()
        if papa_aux != None:
            return papa_aux.padre()
    
    def abuelaPaterna(self):
        papa_aux = self.padre()
        if papa_aux != None:
            return papa_aux.madre()
    
    def tieneAncestro(self, unMamifero):
        papi, mami = self.padre(), self.madre()

        if((mami == unMamifero) or (papi == unMamifero)):
            return True

        if papi == None:
            return False
        else:
            anP = papi.tieneAncestro(unMamifero)
        
        if mami == None:
            return False
        else:
            anM = mami.tieneAncestro(unMamifero)
        
        return anM or anP

def main():
    m1 = Mamifero(1, "Alexa", 3)
    return m1

if __name__ == "__main__":
    main()