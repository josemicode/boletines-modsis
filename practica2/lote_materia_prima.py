import random

class LoteMateriaPrima:
    # productor: Productor
    # fecha_cosecha: date
    # llegada_planta: datetime
    def __init__(self, productor, fecha_cosecha, llegada_planta):
        self._productor = productor
        self._fecha_cosecha = fecha_cosecha
        self._llegada_planta = llegada_planta
        self._codigo = self.codegen()
        self._peso_bruto = None
        self._peso_tara = None
        #self._producto = None

    # Getters
    def getProductor(self):
        return self._productor
    
    def getFechaCosecha(self):
        return self._fecha_cosecha
    
    def getLlegadaPlanta(self):
        return self._llegada_planta
    
    # Setters
    #...

    # Code gen
    def codegen(self):
        for i in range(24):
            res += str(random.randint(0, 9))
        return res
    
    # State Methods