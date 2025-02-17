from usuario import Usuario
from datetime import date

'''
- Se desea desarrollar una aplicación para compartir archivos entre usuarios
de una aplicación. De los usuarios se sabe su nombre, email y password. Los
usuarios tienen los archivos organizados en directorios que ellos mismos crean.
Cada directorio puede contener archivos y también otros directorios. De los
directorios se sabe su nombre. Todo archivo de un usuario debe estar dentro de
un directorio. De un archivo se sabe su nombre, fecha de creación, fecha de
modificación y tamaño. Los archivos pueden ser compartidos de dos maneras,
pero solo de una manera a la vez:

- El usuario propietario de un archivo puede definir una lista de usuarios de
la aplicación para que puedan acceder.

- El usuario propietario puede definir el archivo como público, para que
cualquier usuario de la aplicación pueda acceder. Esta manera de
compartir permite definir una fecha límite a partir de la cual el documento
no podrá ser accedido. Si un archivo no tiene definida una manera de ser
compartido, entonces no puede ser accedido mas que por el propietario
del mismo.
'''

def splittest():
    #words = ["aa", "bb", "cc", "dd"]
    path = "aa/bb/cc/dd" #! No poner /aa/bb...
    words = path.split("/")
    print(words)
    final = "/".join(words[1:])
    print(final)

def main():
    #* Directorios
    u1 = Usuario("Jose", "jose@gmail.com", "123123")
    b1 = u1.crearDirectorio("games", "")
    print("Creado? ", b1)
    b2 = u1.crearDirectorio("games", "")
    print("Creado? ", b2)
    b3 = u1.crearDirectorio("rpg", "games")
    print("Creado? ", b3)
    b4 = u1.crearDirectorio("rpg", "games")
    print("Creado? ", b4)
    b5 = u1.crearDirectorio("multiplayer", "games/rpg")
    #b5 = u1.crearDirectorio("a", "games/rpg/multiplayerr")
    print("Creado? ", b5, "\n")
    #print(u1.directorios[0].directorios[1].getNombre())
    #print(u1.directorios)
    #* Archivos
    fecha = date(2025, 1, 1)
    b6 = u1.crearArchivo("buscaminas", fecha, "games")
    print("Nuevo archivo? ", b6)
    b7 = u1.crearArchivo("diablo iv", fecha, "games/rpg")
    print("Nuevo archivo? ", b7)
    b8 = u1.crearArchivo("terraria", fecha, "games/rpg/multiplayer")
    print("Nuevo archivo? ", b8)
    print("\n")

    #* Compartir archivos
    u2 = Usuario("Carmen", "car@hotmail.com", "hola")
    ar1 = u1.directorios[0].archivos[0]  # buscaminas
    ar2 = u1.directorios[0].directorios[0].archivos[0] # diablo
    print("Accede a buscaminas (pre)? ", u2.tieneAcceso(ar1, date(2025, 2, 2)))
    ar1.compartirCon(u2)
    #print(ar1.permitidos)
    print("Accede a buscaminas (propietario)?", u1.tieneAcceso(ar1, date(2025, 2, 2)))
    print("Accede a buscaminas (post)? ", u2.tieneAcceso(ar1, date(2025, 2, 2)))
    ar2.publicar(date(2025, 2, 1))
    print("Accede a diablo (16/1)? ", u2.tieneAcceso(ar2, date(2025, 1, 16)))
    print("Accede a diablo (2/2)? ", u2.tieneAcceso(ar2, date(2025, 2, 2)))
    print()

    #* Funciones Recursivas
    print("Numero de archivos: ", u1.getNumArchivos())
    print("Tamano total: ", u1.getTamanoTotal())

'''
- Controlar que dado un usuario y un archivo, el usuario pueda acceder al archivo.
- Dado un usuario, retornar la cantidad de archivos que tiene.
- Dado un usuario, retornar el tamaño total ocupado por sus archivos.
'''

if __name__ == "__main__":
    main()

#? TODO:
#* Testear creacion de directorios      [x]
#* Implementar creacion de archivos     [x]
#* Testear creacion de archivos         [x]

#! TODO:
#* Funcion cantidad de archivos         [x]
#* Funcion espacio total ocupado        [x]
#* Compartir archivos                   [x]