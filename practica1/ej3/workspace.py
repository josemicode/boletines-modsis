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

def main():
    #words = ["aa", "bb", "cc", "dd"]
    path = "aa/bb/cc/dd" #! No poner /aa/bb...
    words = path.split("/")
    print(words)
    final = "/".join(words[1:])
    print(final)

'''
- Controlar que dado un usuario y un archivo, el usuario pueda acceder al archivo.
- Dado un usuario, retornar la cantidad de archivos que tiene.
- Dado un usuario, retornar el tamaño total ocupado por sus archivos.
'''

if __name__ == "__main__":
    main()