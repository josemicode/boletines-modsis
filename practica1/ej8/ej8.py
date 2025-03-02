from datetime import datetime, timedelta

class Integrante:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.puntaje = 0
        self.tareas_asignadas = []

    def asignar_tarea(self, tarea):
        self.tareas_asignadas.append(tarea)

    def calcular_puntaje(self, tarea):
        puntaje = calcular_puntaje_tarea(tarea)
        print(f"Calculando puntaje para {self.nombre} en tarea {tarea.titulo}: {puntaje}")
        return puntaje

    def __str__(self):
        return f"{self.nombre} ({self.correo}) - Puntaje: {self.puntaje}"

class Tarea:
    def __init__(self, titulo, descripcion, fecha_tope, complejidad, tipo):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = datetime.now()
        self.fecha_tope = fecha_tope
        self.fecha_cierre = None
        self.complejidad = complejidad
        self.tipo = tipo  
        self.asignaciones = []
        self.lista = None 

    def asignar_integrante(self, integrante, fecha_asignacion):
        # Si ya hay una asignación previa, cerramos la anterior
        if self.asignaciones:
            self.asignaciones[-1].fecha_cierre = datetime.now()
        asignacion = Asignacion(integrante, self, fecha_asignacion)
        self.asignaciones.append(asignacion)
        integrante.asignar_tarea(self)
        print(f"Tarea '{self.titulo}' asignada a {integrante.nombre} en {fecha_asignacion}")

    def finalizar_tarea(self):
        self.fecha_cierre = datetime.now()
        print(f"Tarea '{self.titulo}' finalizada")

    def mover_lista(self, nueva_lista):
        self.lista = nueva_lista
        print(f"Tarea '{self.titulo}' movida a la lista '{nueva_lista.nombre}'")

    def __str__(self):
        return f"Tarea: {self.titulo} | Tipo: {self.tipo} | Fecha Tope: {self.fecha_tope}"

class Asignacion:
    def __init__(self, integrante, tarea, fecha_asignacion):
        self.integrante = integrante
        self.tarea = tarea
        self.fecha_asignacion = fecha_asignacion
        self.fecha_cierre = None
        print(f"Asignación creada para {integrante.nombre} en tarea '{tarea.titulo}'")

class ListaTareas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        tarea.lista = self
        print(f"Tarea '{tarea.titulo}' agregada a la lista '{self.nombre}'")

    def mover_tarea(self, tarea, nueva_lista):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            nueva_lista.agregar_tarea(tarea)
            print(f"Tarea '{tarea.titulo}' movida de lista '{self.nombre}' a '{nueva_lista.nombre}'")

    def __str__(self):
        return f"Lista: {self.nombre} | Tareas: {len(self.tareas)}"

class Tablero:
    def __init__(self, nombre, lider):
        self.nombre = nombre
        self.lider = lider
        self.listas = []
        self.crear_lista("Backlog")

    def crear_lista(self, nombre_lista):
        nueva_lista = ListaTareas(nombre_lista)
        self.listas.append(nueva_lista)
        print(f"Lista '{nombre_lista}' creada en el tablero")

    def crear_tarea(self, titulo, descripcion, fecha_tope, complejidad, tipo):
        tarea = Tarea(titulo, descripcion, fecha_tope, complejidad, tipo)
        # Asigna la tarea a la lista Backlog por defecto
        self.listas[0].agregar_tarea(tarea)
        print(f"Tarea '{titulo}' creada y agregada al Backlog")
        return tarea

    def asignar_tarea(self, tarea, integrante, fecha_asignacion):
        tarea.asignar_integrante(integrante, fecha_asignacion)

    def mover_tarea(self, tarea, lista_destino):
        for lista in self.listas:
            if tarea in lista.tareas:
                lista.mover_tarea(tarea, lista_destino)

    def listar_tareas_pendientes(self):
        tareas_pendientes = []
        for lista in self.listas:
            for tarea in lista.tareas:
                if tarea.fecha_cierre is None:
                    tareas_pendientes.append(tarea)
        tareas_pendientes.sort(key=lambda t: t.fecha_creacion)  # Ordenar por fecha de creación
        print("Tareas pendientes listadas:")
        for tarea in tareas_pendientes:
            print(tarea)
        return [str(tarea) for tarea in tareas_pendientes]

    def listar_tareas_usuario(self, usuario):
        tareas_usuario = []
        for lista in self.listas:
            for tarea in lista.tareas:
                for asignacion in tarea.asignaciones:
                    if asignacion.integrante == usuario:
                        tareas_usuario.append(tarea)
        print(f"Tareas de {usuario.nombre}:")
        for tarea in tareas_usuario:
            print(tarea)
        return tareas_usuario

    def cerrar_sprint(self):
        fecha_limite = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        fecha_inicio = fecha_limite - timedelta(days=15)

        # Asignar puntajes a tareas completadas dentro de los últimos 15 días
        for lista in self.listas:
            for tarea in lista.tareas:
                if tarea.fecha_cierre and tarea.fecha_cierre >= fecha_inicio:
                    # Asignar puntaje al responsable de la tarea
                    for asignacion in tarea.asignaciones:
                        integrante = asignacion.integrante
                        puntaje_tarea = integrante.calcular_puntaje(tarea)
                        integrante.puntaje += puntaje_tarea

                    # Si es una tarea de DIU, el líder también obtiene puntos si se completó a tiempo
                    if tarea.tipo == 'DIU' and tarea.fecha_cierre <= tarea.fecha_tope:
                        self.lider.puntaje += 1
                        print(f"Líder {self.lider.nombre} obtiene 1 punto por tarea DIU completada a tiempo")

    def __str__(self):
        return f"Tablero: {self.nombre} | Líder: {self.lider.nombre}"

def calcular_puntaje_tarea(tarea):
    if tarea.tipo == 'DIU':
        if tarea.fecha_cierre and tarea.fecha_cierre <= tarea.fecha_tope:
            print(f"Tarea DIU '{tarea.titulo}' completada a tiempo, puntaje: {2 * tarea.complejidad}")
            return 2 * tarea.complejidad
        else:
            print(f"Tarea DIU '{tarea.titulo}' no completada a tiempo, puntaje: 1")
            return 1
    elif tarea.tipo == 'Programación':
        if tarea.fecha_cierre and tarea.fecha_cierre <= tarea.fecha_tope:
            print(f"Tarea de Programación '{tarea.titulo}' completada a tiempo, puntaje: {tarea.complejidad ** 2}")
            return tarea.complejidad ** 2
        else:
            print(f"Tarea de Programación '{tarea.titulo}' no completada a tiempo, puntaje: 0")
            return 0
    return 0
