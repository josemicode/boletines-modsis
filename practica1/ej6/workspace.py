from ej6 import *


def main():
    # Crear repuestos
    repuesto1 = Repuesto("Filtro de aire", 100)
    repuesto2 = Repuesto("Aceite motor", 50)
    repuesto3 = Repuesto("Bujía", 30)
    print("\n")
    
    # Crear trenes
    tren1 = Tren("12345", "Modelo A", "Marca X", date(2020, 1, 1), 50000)
    tren2 = Tren("67890", "Modelo B", "Marca Y", date(2022, 5, 15), 20000)
    print("\n")

    # Crear tareas por tiempo
    tarea1 = TareaPorTiempo("T1", 2, 200, [repuesto1, repuesto2], 30)  # cada 30 días
    tarea2 = TareaPorTiempo("T2", 3, 150, [repuesto3], 180)  # cada 180 días
    print("\n")

    # Crear tareas por rodadura
    tarea3 = TareaPorRodadura("T3", 1, 500, [repuesto1, repuesto3], 10000)  # cada 10,000 km
    tarea4 = TareaPorRodadura("T4", 4, 700, [repuesto2], 20000)  # cada 20,000 km
    print("\n")

    # Crear plan de mantenimiento y agregar tareas
    plan_mantenimiento = PlanDeMantenimiento("1.0", "Modelo A")
    plan_mantenimiento.agregarTarea(tarea1)
    plan_mantenimiento.agregarTarea(tarea2)
    plan_mantenimiento.agregarTarea(tarea3)
    plan_mantenimiento.agregarTarea(tarea4)
    print("\n")

    # Crear sistema
    sistema = Sistema()
    print("\n")

    # Registrar trenes y plan de mantenimiento
    sistema.registrarTren(tren1)
    sistema.registrarTren(tren2)
    sistema.registrarPlanMant(plan_mantenimiento)
    print("\n")

    # Asignar plan de mantenimiento a los trenes
    tren1.setPlanMantenimiento(plan_mantenimiento)
    tren2.setPlanMantenimiento(plan_mantenimiento)
    print("\n")

    # Registrar viajes
    viaje1 = Viaje(date(2025, 3, 2), 3000)  # 3000 km recorridos
    viaje2 = Viaje(date(2025, 3, 5), 1500)  # 1500 km recorridos
    print("\n")

    sistema.registrarViaje("12345", viaje1)
    sistema.registrarViaje("12345", viaje2)
    print("\n")

    # Obtener tareas pendientes de un tren (tren1)
    tareas_pendientes_tren1 = plan_mantenimiento.getTareasPendientes(tren1)
    print(f"Tareas pendientes para el tren {tren1.getNumeroSerie()}:")
    for tarea in tareas_pendientes_tren1:
        print(f" - {tarea.getIdTarea()}")
    print("\n")

    # Registrar tareas realizadas
    for tarea in tareas_pendientes_tren1:
        sistema.registrarTareaReal(tren1, tarea, "Mantenimiento rutinario", date(2025, 3, 2))
    print("\n")

    # Obtener el costo mensual de un tren (por ejemplo, tren1, marzo 2025)
    costo_mensual_tren1 = sistema.getCosteMensualTren(tren1, 3, 2025)
    print(f"Costo total de mantenimiento del tren {tren1.getNumeroSerie()} en marzo 2025: {costo_mensual_tren1}")
    print("\n")

    # Obtener los 5 planes de mantenimiento más caros
    planes_caros = sistema.get5PlanesMasCaros()
    print("Los 5 planes de mantenimiento más caros:")
    for plan in planes_caros:
        print(f" - Plan {plan.getVersion()} para el modelo {plan.getModelo()}")
    print("\n")


if __name__ == "__main__":
    main()

