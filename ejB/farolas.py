class Farola:
    def __init__(self, id, estadoBooleano):
        self.id = id
        self.estado = estadoBooleano
        self.vecinas = []
    
    def vincular(self, farolaVecina):
        if farolaVecina not in self.vecinas:
            self.vecinas.append(farolaVecina)
            farolaVecina.vincular(self)
    
    def toString(self):
        return (str(self.id) + " -> " + str(self.estado))
    
    def listarVecinas(self):
        for farola in self.vecinas:
            print(farola.toString())
    
    def interruptor(self, nuevoEstado):
        if self.estado == nuevoEstado:
            return
        
        self.estado = nuevoEstado
        
        for farola in self.vecinas:
            farola.interruptor(nuevoEstado)

def main():
    f1, f2, f3, f4 = Farola(1, 0), Farola(2, 0), Farola(3, 0), Farola(4, 0)
    f1.vincular(f2)
    f1.vincular(f3)
    f2.vincular(f3)
    f3.vincular(f4)
    
    f4.interruptor(1)
    #f2.interruptor(1)
    #f3.interruptor(0)
    
    print("f2:")
    f1.listarVecinas()
    print("f2:")
    f2.listarVecinas()
    print("f3:")
    f3.listarVecinas()
    print("f4:")
    f4.listarVecinas()

if __name__ == "__main__":
    main()
