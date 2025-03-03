   
from datetime import date
from abc import ABC, abstractmethod  

class Tren():
    def __init__(self, numero_serie, modelo, marca, fecha_incorporacion, km_inicial):
        self.numero_serie = numero_serie
        self.modelo = modelo
        self.marca = marca
        self.fecha_incorporacion = fecha_incorporacion
        self.km_inicial = km_inicial
        self.viajes = []  
        self.plan_mantenimiento = None
        print(f"Tren {self.numero_serie} ({self.modelo}) creado correctamente.")

    def getNumeroSerie(self):
        return self.numero_serie
    
    def getModelo(self):
        return self.modelo
    
    def getMarca(self):
        return self.marca
    
    def getFechaIncorporacion(self):
        return self.fecha_incorporacion
    
    def getKmInicial(self):
        return self.km_inicial
    
    def getViajes(self):
        return self.viajes
    
    def getPlanMantenimiento(self):
        return self.plan_mantenimiento
    
    def setPlanMantenimiento(self, plan):
        self.plan_mantenimiento = plan
        print(f"Plan de mantenimiento '{plan.version}' asignado al tren {self.numero_serie}.")
    
    def registrarViaje(self, viaje):
        self.viajes.append(viaje)
        print(f"Viaje registrado para el tren {self.numero_serie} con {viaje.km_recorridos} km recorridos.")
    
    def getUltimoKilometraje(self):
        km_total = self.km_inicial + sum(viaje.km_recorridos for viaje in self.viajes)
        print(f"Kilometraje total del tren {self.numero_serie}: {km_total} km.")
        return km_total


class Viaje():
    def __init__(self, fecha_viaje, km_recorridos):
        self.fecha_viaje = fecha_viaje
        self.km_recorridos = km_recorridos
        print(f"Viaje registrado para el día {self.fecha_viaje} con {self.km_recorridos} km recorridos.")
    
    def getFechaViaje(self):
        return self.fecha_viaje
    
    def getKmRecorridos(self):
        return self.km_recorridos


class PlanDeMantenimiento():
    def __init__(self, version, modelo_asociado):
        self.version = version
        self.modelo_asociado = modelo_asociado
        self.tareas = []
        print(f"Plan de mantenimiento {self.version} para el modelo {self.modelo_asociado} creado.")
        
    def agregarTarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.getIdTarea()}' agregada al plan de mantenimiento {self.version}.")
  
    def getVersion(self):
        return self.version
    
    def getModelo(self):
        return self.modelo_asociado
    
    def getTareasPendientes(self, tren):
        tareas_pendientes = []
        print(f"Verificando tareas pendientes para el tren {tren.getNumeroSerie()}.")
        for tarea in self.tareas:
            if isinstance(tarea, TareaPorTiempo):
                dias_transcurridos = (date.today() - tren.fecha_incorporacion).days
                print(f"Verificando tarea por tiempo '{tarea.getIdTarea()}': {dias_transcurridos} días transcurridos.")
                if dias_transcurridos % tarea.periodicidad == 0:
                    tareas_pendientes.append(tarea)
            
            elif isinstance(tarea, TareaPorRodadura):
                km_recorridos = tren.getUltimoKilometraje()  # Este es el kilometraje total hasta ahora
                print(f"Verificando tarea por rodadura '{tarea.getIdTarea()}': {km_recorridos} km recorridos.")
                if km_recorridos >= tarea.km_intervalo:
                    tareas_pendientes.append(tarea)
        
        print(f"Tareas pendientes encontradas: {len(tareas_pendientes)}")
        return tareas_pendientes


class TareaDeMantenimiento(ABC):
    def __init__(self, id_tarea, tiempo_estimado, costo_base, repuestos):
        self.id_tarea = id_tarea
        self.tiempo_estimado = tiempo_estimado
        self.costo_base = costo_base
        self.repuestos = repuestos  
        print(f"Tarea '{self.id_tarea}' de mantenimiento creada.")
    
    @abstractmethod
    def calcularCosto(self, km_recorridos=None):
        pass
    
    def getIdTarea(self):
        return self.id_tarea
    
    def getTiempoEstimado(self):
        return self.tiempo_estimado
    
    def getCostoBase(self):
        return self.costo_base
    
    def getRepuestos(self):
        return self.repuestos


class TareaPorTiempo(TareaDeMantenimiento):
    def __init__(self, id_tarea, tiempo_estimado, costo_base, repuestos, periodicidad):
        super().__init__(id_tarea, tiempo_estimado, costo_base, repuestos)
        self.periodicidad = periodicidad  # En dias
        print(f"Tarea por tiempo '{self.id_tarea}' creada con periodicidad de {self.periodicidad} días.")
    
    def calcularCosto(self, km_recorridos=None):
        costo_total = self.costo_base + sum(repuesto.costo for repuesto in self.repuestos)
        print(f"Costo total de la tarea '{self.id_tarea}': {costo_total}.")
        return costo_total
    
    def getPeriodicidad(self):
        return self.periodicidad


class TareaPorRodadura(TareaDeMantenimiento):
    def __init__(self, id_tarea, tiempo_estimado, costo_base, repuestos, km_intervalo):
        super().__init__(id_tarea, tiempo_estimado, costo_base, repuestos)
        self.km_intervalo = km_intervalo  # Cada cuantos km se realiza
        print(f"Tarea por rodadura '{self.id_tarea}' creada con intervalo de {self.km_intervalo} km.")
    
    def calcularCosto(self, km_recorridos):
        if km_recorridos is None:
            raise ValueError("Debe proporcionar los kilómetros recorridos para calcular el costo.")
        
        costo_total = self.costo_base + (0.05 * km_recorridos) + sum(repuesto.costo for repuesto in self.repuestos)
        print(f"Costo total de la tarea por rodadura '{self.id_tarea}' con {km_recorridos} km recorridos: {costo_total}.")
        return costo_total
    
    def getKmIntervalo(self):
        return self.km_intervalo


class Repuesto:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
        print(f"Repuesto '{self.nombre}' con costo de {self.costo} creado.")
        
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getCosto(self):
        return self.costo

    def setCosto(self, costo):
        self.costo = costo


class RegistroMantenimiento:
    def __init__(self, tren, tarea, fecha, descripcion, costo):
        self.tren = tren
        self.tarea = tarea
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        print(f"Registro de mantenimiento para el tren {self.tren.getNumeroSerie()} realizado el {self.fecha} con costo de {self.costo}.")
    
    def getTren(self):
        return self.tren

    def setTren(self, tren):
        self.tren = tren

    def getTarea(self):
        return self.tarea

    def setTarea(self, tarea):
        self.tarea = tarea

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getCosto(self):
        return self.costo

    def setCosto(self, costo):
        self.costo = costo


class Sistema():
    def __init__(self):
        self.trenes = [] 
        self.planes_mantenimiento = []  
        self.tareas_mantenimiento = []  
        self.registros_mantenimiento = [] 
        print("Sistema de mantenimiento inicializado.")
    
    def registrarTren(self, tren):
        self.trenes.append(tren)
        print(f"Tren {tren.getNumeroSerie()} registrado en el sistema.")
    
    def registrarPlanMant(self, plan):
        self.planes_mantenimiento.append(plan)
        print(f"Plan de mantenimiento '{plan.getVersion()}' registrado en el sistema.")
    
    def agregarTareaPlan(self, version, tarea):
        for plan in self.planes_mantenimiento:
            if plan.version == version:
                plan.agregarTarea(tarea)
                return
        print(f"El plan de mantenimiento con versión {version} no existe.")
    
    def registrarViaje(self, num_serie, viaje):
        for t in self.trenes:
            if t.numero_serie == num_serie:
                t.registrarViaje(viaje)
                return
        print(f"El tren con número de serie {num_serie} no está registrado.")
    
    def registrarTareaReal(self, tren, tarea, descripcion, fecha):
        costo_total = tarea.calcularCosto(tren.getUltimoKilometraje())
        registro = RegistroMantenimiento(tren, tarea, fecha, descripcion, costo_total)
        self.registros_mantenimiento.append(registro)
        print(f"Tarea '{tarea.getIdTarea()}' registrada como realizada para el tren {tren.getNumeroSerie()}.")

    def getCosteMensualTren(self, tren, mes, anio):
        costo_total = 0
        for registro in self.registros_mantenimiento:
            if registro.tren == tren and registro.fecha.month == mes and registro.fecha.year == anio:
                costo_total += registro.costo
        print(f"Costo total de mantenimiento para el tren {tren.getNumeroSerie()} en {mes}/{anio}: {costo_total}.")
        return costo_total

    def get5PlanesMasCaros(self):
        costos = []
        for plan in self.planes_mantenimiento:
            costo_total = 0
            for tarea in plan.tareas:
                costo_total += tarea.costo_base + sum(repuesto.costo for repuesto in tarea.repuestos)
            costos.append((plan, costo_total))
        costos.sort(key=lambda x: x[1], reverse=True)
        print("Los 5 planes de mantenimiento más caros son:")
        return [plan for plan, _ in costos[:5]]

