from productor import Productor
from lote_materia_prima import LoteMateriaPrima
from datetime import date, datetime
#import uuid

def main():
    p1 = Productor("Juan", "Perez", "12345678A", "Calle Falsa 123", "123456789", "abc@gmail.com")
    lmp1 = LoteMateriaPrima(p1, date(2025, 1, 1), datetime.now())

    print(lmp1.getCodigo())

if __name__ == "__main__":
    main()