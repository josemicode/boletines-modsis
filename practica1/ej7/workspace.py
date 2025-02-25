'''
Se desea una plataforma para encontrar trabajos de manera freelance (es
decir, por cuenta propia). En dicha plataforma, quienes requieren que se efectúe
un trabajo (por ejemplo, desarrollar una aplicación) lo publican como un proyecto
y quienes buscan trabajos (los freelancers) se ofrecen a desarrollar alguno de
esos proyectos publicados. La aplicación debe resolver la asignación entre
proyectos y freelancers.
Cuando un proyecto se publica, acepta ofertas de freelancers hasta una
fecha específica. Las ofertas son cotización que pueden hacerse de dos
maneras, por hora de trabajo o por posición. Luego, la aplicación asigna un
freelancer en función de la mejor oferta, que se determina según el costo final de
desarrollo. Una vez hecha la asignación, la plataforma se desliga de su
desarrollo, aunque permite al proyectista establecer que el proyecto fue
terminado para que el freelancer sume los puntos correspondientes.
'''

from datetime import date
from sistema import Sistema
from proyecto import Proyecto
from proyectista import Proyectista
from freelancer import Freelancer
from ofertas import OfertaPorHora, OfertaPorPosicion
from categorias import Categoria

def main():
    # Registrar un proyectista
    proyectista = Proyectista("Juan Perez", "juan.perez@example.com")

    # Registrar un freelancer
    freelancer = Freelancer("Ana Gomez", "ana.gomez@example.com", 50, [Categoria.WEB, Categoria.DG])

    # Registrar un proyecto y asignar a proyectista
    proyecto = Proyecto("Desarrollo Web", "Desarrollar una página web", date(2023, 12, 31), Categoria.WEB)
    proyectista.asignarProyecto(proyecto)

    # Registrar oferta para proyecto (por hora de trabajo)
    oferta_por_hora = OfertaPorHora(date(2023, 11, 1), 100, date(2023, 12, 15), freelancer.getPrecioHora())

    # Registrar oferta para proyecto (por posición de trabajo)
    oferta_por_posicion = OfertaPorPosicion(date(2023, 11, 1), 2000, 160, 2)

    # Crear sistema y agregar freelancers y ofertas
    sistema = Sistema([freelancer], [oferta_por_hora, oferta_por_posicion])

    # Buscar un proyecto por categoría
    proyectos_web = proyectista.getProyectosPorCategoria(Categoria.WEB)
    print("Proyectos en la categoría WEB:")
    for pr in proyectos_web:
        print(pr)

    # Buscar un freelancer por categoría
    freelancers_web = sistema.getFreelancersPorCategoria(Categoria.WEB)
    print("Freelancers en la categoría WEB:")
    for fr in freelancers_web:
        print(fr)

    # Recomendar oferta de proyectos
    print("Ofertas ordenadas por puntaje:")
    sistema.ordenarOfertasPorPuntaje()
    ofertas_ordenadas = sistema.getOfertas()
    for of in ofertas_ordenadas:
        print(of)
    #sistema.listarOfertas()

    # Asignar oferta a un proyecto
    proyecto.asignarOferta(oferta_por_hora, date(2023, 11, 2))
    proyecto.asignarFreelancer(freelancer)

    # Retornar el freelancer asignado a un proyecto
    freelancer_asignado = proyecto.getFreelancer().getNombre()
    print(f"Freelancer asignado al proyecto: {freelancer_asignado}")

    # Registrar finalización de proyecto
    proyecto.finalizar()
    print(f"Proyecto finalizado con puntaje: {freelancer.puntaje}")

'''
- Registrar un <proyectista>: Se le indica el nombre del proyectista y su
dirección de email.
- Registrar un <freelancer>: Se le indica el nombre del freelancer, su dirección
de email, el precio de hora de trabajo, y las categorías (ej.: Desarrollo
Web, Diseño Gráfico, etc.).
- Registrar un <proyecto>: Se indica el nombre, la descripción, la fecha hasta
la que se aceptan ofertas.
- Registrar oferta para <proyecto>: para brindarle flexibilidad a cada freelancer
a la hora de cotizar los proyectos según aspectos profesionales no
contemplados en la aplicación, las ofertas de trabajo pueden ser:
    - por hora de trabajo: Una oferta por hora de trabajo implica que el
    freelancer cotiza el proyecto en función de las horas especificadas
    en su oferta y su propio precio por hora de trabajo. Se requiere
    saber la fecha de la oferta, la cantidad de horas estimadas y la
    fecha de entrega estimada.
    - por posición de trabajo: Una oferta por posición implica que el
    freelancer cotiza el proyecto en función de cobrar un sueldo
    mensual por una cantidad de horas de trabajo por mes por una
    cantidad de meses determinada.
- Buscar un proyecto por categoría <proyectista>: Se recibe el nombre de una categoría
y retorna los proyectos que la incluyen.
- Buscar un freelancer por categoría <Sist>: Se recibe el nombre de una categoría
y retorna los freelancer que la incluyen.
- Recomendar oferta de proyectos: Para ayudar al <proyectista, Sist> a escoger
una oferta, debe ser posible obtener un listado de ofertas ordenadas por
puntaje. El puntaje de una oferta se define por el precio total dividido la
cantidad de días que deben pasar para la entrega del proyecto:
    - El precio final de una oferta por hora de trabajo es la cantidad de
    horas establecidas por el freelancer multiplicadas por el precio de
    hora de trabajo del mismo.
    - El precio final de una oferta por posición es el salario estipulado
    multiplicado por la cantidad de meses de posición definida.
    - La cantidad de días de entrega para una oferta por hora de trabajo
    es definida por la cantidad de días entre la fecha de inicio
    (considerando como fecha de inicio la fecha en la que el proyecto
    ya no acepta más ofertas) y la fecha de entrega estimada.
    - La cantidad de días de entrega para una oferta por posición es
    definida por la cantidad días entre la fecha de inicio (también
    considerando como fecha de inicio la fecha en la que el proyecto
    ya no acepta más ofertas) y la de fecha finalización, calculada en
    función de los meses de posición definidos en la oferta.
- Asignar oferta a un <proyecto>: dado un proyecto y una oferta del mismo, se
registra asigna como ganadora la oferta al proyecto.
- Retornar el freelancer asignado a un <proyecto>: dado un proyecto, retorna
el freelancer asignado. Si no tiene freelancer asignado, retorna nil.
- Registrar finalización de proyecto: Para un proyecto con freelancer
asignado, el <proyectista> puede registrar la finalización del <proyecto>,
sumando un puntaje del 1 al 50 para el freelancer. Además del puntaje
establecido, también debe registrarse la fecha de finalización del
proyecto.

'''

if __name__ == "__main__":
    main()