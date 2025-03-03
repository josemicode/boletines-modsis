from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Abono(ABC):
    def __init__(self):
        self.activo = True

    @abstractmethod
    def calcularCoste(self, tiempo_uso):
        pass

    def esValido(self):
        return self.activo

class AbonoAnual(Abono):
    def __init__(self, fecha_inicio):
        super().__init__()
        self.fecha_inicio = fecha_inicio
        self.precio = 100

    def calcularCoste(self, tiempo_uso):
        if tiempo_uso > 30:
            exceso = tiempo_uso - 30
            return (exceso // 5) * 2
        return 0
    
    def esValido(self):
        return datetime.now() - self.fecha_inicio < timedelta(days=365)

class AbonoPrepago(Abono):
    def __init__(self, saldo):
        super().__init__()
        self.saldo = saldo

    def calcularCoste(self, tiempo_uso):
        costo = (tiempo_uso // 15) * 5
        self.saldo -= costo
        return costo
    
    def esValido(self):
        return self.saldo >= -5

class AbonoTuristico(Abono):
    def __init__(self, fecha_inicio):
        super().__init__()
        self.fecha_inicio = fecha_inicio
        self.precio = 10

    def calcularCoste(self, tiempo_uso):
        if tiempo_uso > 120:
            exceso = tiempo_uso - 120
            return (exceso // 15) * 10
        return 0
    
    def esValido(self):
        return datetime.now() - self.fecha_inicio < timedelta(days=7)

class Usuario():
    def __init__(self, dni, nombre, tarjeta_credito):
        self.dni = dni
        self.nombre = nombre 
        self.tarjeta_credito = tarjeta_credito 
        self.abono = None 
        self.uso_bici = False
        
    def RegistrarAbono(self, abono):
        if isinstance(abono, AbonoAnual) or isinstance(abono, AbonoTuristico):
            pago_exitoso = Pago.procesarPago(self.tarjeta_credito, abono.precio)
            if not pago_exitoso:
                print("Pago rechazado. No se puede asignar el abono.")
                return
        
        self.abono = abono
        print(f"Abono {abono.__class__.__name__} registrado correctamente.")

    #!Quitar
    def RecogerBicicleta(self, estacion):
        if self.uso_bici:
            print("Ya tienes una bicicleta en uso.")
            return
        
        if estacion.bicicletas_disponibles > 0:
            self.uso_bici = True
            estacion.bicicletas_disponibles -= 1
            estacion.estacionamientos_libres += 1
            print(f"{self.nombre} ha tomado una bicicleta de la estación {estacion.ubicacion}.")
        else:
            print("No hay bicicletas disponibles en esta estación.")

    def devolverBicicleta(self, estacion, tiempo_uso):
        if not self.uso_bici:
            print("No tienes ninguna bicicleta en uso.")
            return
        
        self.uso_bici = False
        estacion.bicicletas_disponibles += 1
        estacion.estacionamientos_libres -= 1
        print(f"{self.nombre} ha devuelto una bicicleta en la estación {estacion.ubicacion}.")
        
        if self.abono:
            costo = self.abono.calcularCoste(tiempo_uso)
            if costo > 0:
                Pago.procesarPago(self.tarjeta_credito, costo)
                print(f"Se ha cobrado un total de {costo}€ por el uso.")
                

class Estacion():
    def __init__(self, ubicacion, capacidad, bicicletas_disponibles, estacionamientos_libres):
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.bicicletas_disponibles = bicicletas_disponibles
        self.estacionamientos_libres = estacionamientos_libres
   
    def usarBicicleta(self, usuario):
        if self.bicicletas_disponibles > 0 and not usuario.uso_bici:
            self.bicicletas_disponibles -= 1
            self.estacionamientos_libres += 1
            usuario.uso_bici = True
            return True
        return False
    
    def devolverBicicleta(self, usuario):
        if self.estacionamientos_libres > 0 and usuario.uso_bici:
            self.bicicletas_disponibles += 1
            self.estacionamientos_libres -= 1
            usuario.uso_bici = False
            return True
        return False
    
    def tieneBicicletasDisponibles(self):
        return self.bicicletas_disponibles > 0
    
    def tieneEstacionamientosDisponibles(self):
        return self.estacionamientos_libres > 0
    
    
    @staticmethod
    def estaciones_con_bicicletas_disponibles(estaciones):
        return [estacion for estacion in estaciones if estacion.tieneBicicletasDisponibles()]

    @staticmethod
    def estaciones_con_estacionamientos_libres(estaciones):
        return [estacion for estacion in estaciones if estacion.tieneEstacionamientosDisponibles()]
    
    
class UsoBicicleta:
    def __init__(self, usuario, bicicleta, estacion_recogida):
        self.usuario = usuario
        self.bicicleta = bicicleta
        self.estacion_recogida = estacion_recogida
        self.fecha_hora_recogida = datetime.now()
        self.estacion_devolucion = None
        self.fecha_hora_devolucion = None
    
    def devolverBicicleta(self, estacion_devolucion):
        self.estacion_devolucion = estacion_devolucion
        self.fecha_hora_devolucion = datetime.now()
        
        tiempo_uso = (self.fecha_hora_devolucion - self.fecha_hora_recogida).total_seconds() / 60  # Minutos
        
        # Cobrar si supera 24 horas (1440 minutos)
        if tiempo_uso > 1440:
            Pago.procesarPago(self.usuario.tarjeta_credito, 30)
            print("Se ha cobrado una penalización de 30€ por superar las 24 horas de uso.")
        
        return tiempo_uso

class Bicicleta:
    def __init__(self, id_bicicleta):
        self.id_bicicleta = id_bicicleta
        self.en_uso = False
        self.estacion_actual = None
    
    def asignarEstacion(self, estacion):
        if not self.en_uso:
            self.estacion_actual = estacion
    
    def recoger(self):
        if not self.en_uso:
            self.en_uso = True
            self.estacion_actual = None
            return True
        return False
    
    def devolver(self, estacion):
        if self.en_uso:
            self.en_uso = False
            self.estacion_actual = estacion
            return True
        return False

class Pago:
    @staticmethod
    def procesarPago(tarjeta_credito, coste):
        print(f"Se ha procesado un pago de {coste}€ con la tarjeta {tarjeta_credito}.")
        return True
    