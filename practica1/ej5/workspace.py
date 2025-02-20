'''
Una empresa requiere una plataforma para que diseñadores y creadores
puedan comercializar por allí sus diseños y recursos (imágenes, íconos,
tipografías, templates web, etc.). Cada vez que un creador de recursos registra
una nueva producción, puede configurar una estrategia de comercialización, que
son ideadas por los propietarios de la plataforma. Los creadores de recursos
juntan puntos cada vez que un usuario adquiere uno de sus productos. Y estos
puntos sirven a la plataforma no solo para posicionar a los creadores dentro de
la misma sino también para computar su costo de suscripción a la plataforma en
un futuro.
'''

def main():
    pass

'''
- Registrar nuevo creador de recursos: se indica su nombre, email,  
contraseña y se inicia con 0 su cantidad de puntos.
- Registrar un nuevo recurso: se indica el creador, una descripción del
recurso, una imagen de previsualización, una URL de descarga, fecha de
carga, su precio base y una estrategia de comercialización (que no podrán
cambiar en el futuro), que inicialmente puede ser:
    - Normal: implica que los usuarios podrán descargar el recurso
    pagando el costo base del recurso.
    - Oferta: se define una fecha límite y un porcentaje de descuento. Si
    una compra se realiza antes de la fecha límite se aplica el
    porcentaje de descuento, mientras que luego de dicha fecha se
    cobra el costo base completo.
    - Crowd-based: se define una cantidad de usuarios mínimos que
    deben comprar el recurso. Solo cuando la cantidad de usuarios que
    lo compran alcanza al menos ese límite, dichos compradores
    podrán descargarlo, y se realizará el cobro considerando el precio
    base del recurso.
- Registrar nuevo usuario: se indica su nombre, email y contraseña.
- Registrar una nueva compra de recurso: se indica el usuario y el recurso
a adquirir. Cuando se crea una nueva compra, deben pasar varias cosas:
    - Calcular el costo de la compra, la cual depende de la estrategia de
    comercialización del producto.
    - Calcular y registrar la cantidad de puntos que el creador sumará,
    que se calcula también según la estrategia de comercialización:
        - i. Normal: el puntaje resulta del costo base * 10.
        - ii. Oferta: el puntaje resulta de costo de la compra * 5 cuando
        la oferta aun no venció, y * 10 cuando ya ha vencido.
        - iii. Crowd-based: el puntaje resulta de multiplicar el costo
        base * 50 / la cantidad de usuarios mínimos.
'''

if __name__ == "__main__":
    pass