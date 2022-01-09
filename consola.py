#ABRIR ARCHIVO Y ESCRIBIR EN EL, CON PARTICIPACION DE USUARIO
import os, shutil, ntpath
from os import rmdir

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
  
CREAR_CARPETA = 1
UBICACION = 2
TAMAÑO = 3
CAMBIAR_UBI = 4
ARCHIVO = 5
FILTAR = 6
REENOMBRAR_ARC = 7
ELIMINAR = 8

def menu():
    print(f'''{colors.BOLD}CONSOLA DE COMANDOS{colors.ENDC}
{CREAR_CARPETA}) CREAR CARPETA
{UBICACION}) UBICACION DE TRABAJO
{TAMAÑO}) TAMAÑO
{CAMBIAR_UBI}) CAMBIAR UBICACION DE ARCHIVOS 
{ARCHIVO}) ARCHIVO
{FILTAR }) FILTAR 
{REENOMBRAR_ARC}) REENOMBRAR_ARC
{ELIMINAR}) ELIMINAR CARPETAS O ARCHIVOS''')

def carpeta():
    print("Tu ubicacion actúal:",os.getcwd())
    elc = input(f"{colors.BOLD}Deseas crear la carpeta aqui?{colors.ENDC}\n1)Si\n2)No\nEleccion: ")
    try:
        elc = int(elc)
    except:
        print("Inserta un numero!")
        input("Inserte enter para continuar..")
        os.system("cls")
    if elc == 1 or elc == 2:
        if elc == 1:
            name = input("Inserta nombre de la carpeta: ")
            os.mkdir(name)
            print("Carpeta creada con exito!")
            input("Presione enter para continuar...")
            os.system("cls")
        if elc == 2:
            elc = input(f"{colors.BOLD}¿Tienes una ruta en especifico?{colors.ENDC}\n1)Si\n2)No\nEleccion: ")
            try:
                elc = int(elc)
            except:
                print("Inserta un numero!")
                input("Inserte enter para continuar..")
                os.system("cls")
            if elc == 1:
                path = input("Inserta la ruta:")
                try:
                    os.chdir(path)
                except OSError:
                    print("La creación del directorio %s falló" % name)
                else:
                    name = input("Inserta nombre de la carpeta: ")
                    os.mkdir(name)
                    print("Se ha creado el directorio: %s " % name)
                input("Inserte enter para continuar...")
                os.system("cls")
            if elc == 2:
                input("Vuelva a intentarlo...")
                os.system("cls")
    else:
        input("Inserte enter para continuar...")
        os.system("cls")
        
def ubicacion():
    print("Tu ubicacion actual es:", os.getcwd())
    input("Inserte enter para continuar..")
    os.system("cls")

def tamanio():
    path = input("Inserte la ruta del archivo: ")
    try :
        size = os.path.getsize(path)
    except OSError :
        print("Path '%s' does not exists or is inaccessible" %path)
        os.sys.exit()
    print("El tamaño es de:",(size/1024**2), "MB")
    input("Inserte enter para continuar...")
    os.system("cls")
    
def cambiar_ubi():
    while True:
        elc = input("Elija una opcion:\n1)Si\n2)No\nEleccion: ")
        try:
            elc = int(elc)
        except:
            print("Inserta un numero!")
            input("Inserte enter para continuar..")
            os.system("cls")
        if 1 <= elc <= 2:
            if elc == 1:
                print("Tu ubicacion actual es:", os.getcwd())
                path = input(r"Inserta ruta de archivo del cual quieres cambiar ubicacion: ")
                if os.path.exists(path) == True:
                    path1 = input(r"¿A que ruta lo quieres llevar?")
                    if os.path.isdir(path1) == True:
                        shutil.move(path, path1)
                        print("UBICACION CAMBIADA CON EXITO")
                        input("Presione enter para continuar..")
                        os.system("cls")
                        break  
                    else:
                        print("No existe tal ruta...")
                        input("Presione enter para continuar...")
                        os.system("cls")
                        continue
                else:  
                    print("No existe tal ruta...")
                    input("Presione enter para continuar...")
                    os.system("cls")
                    continue    
            if elc == 2:
                elc = input(f"{colors.BOLD}{colors.WARNING}¿Confirmas que quieres salir?{colors.ENDC}\n1)Si\n2)No\nEleccion: ")
                try:
                    elc = int(elc)
                except:
                    print("Inserta un numero!")
                    input("Inserte enter para continuar..")
                    os.system("cls")
                if elc == 1 or elc == 2:
                    if elc == 1:
                        break
                    if elc == 2:
                        os.system("cls")
                        continue
        else:
            print("No se entendio tu eleccion.")
            input("Inserte enter para continuar...")
            os.system("cls")
            continue
        
def archivo():
    while True:
        print(f"{colors.BOLD}MENU{colors.ENDC}\n1)Abrir archivo y escribir\n2)Leer archivo\n3)Salir\nEleccion: ")
        elc= input("Ingresa tu eleccion: ")
        try:
            elc = int(elc)
        except:
            print("Debes ingresar un numero! Vuelve a empezar.")
            input("Ingresa enter para continuar...")
            os.system("cls")
            continue
        if 1 <= elc and elc <= 3:
            if elc == 1:
                path = input("Inserta la ruta del archivo: ")
                archivo = ntpath.basename(path)
                elc = input(f"¿Estas seguro de que quieres abrir {archivo}?\n1)Si\n2)No\nEleccion: ")
                try:
                    elc = int(elc)
                except:
                    print("Debes ingresar un numero! Vuelve a empezar.")
                    input("Presione enter para continuar..")
                    os.system("cls")
                    continue
                if 1 <= elc <= 2: 
                    if elc == 1:
                            archivo = open(path, "w")
                            escritura = input("¿Que deseas escribir en él?: ")
                            archivo.write(escritura)
                            os.system("cls")
                            print("ARCHIVO CREADO CON EXITO")
                    if elc == 2:
                        input("Presione enter para continuar..")
                        os.system("cls")
                        continue  
                else:
                    print("No se ha entendido tu eleccion")
                    input("Presione enter para continuar...")
                    continue
            if elc == 2:
                path = input("Inserta la ruta del archivo: ")
                archivo = ntpath.basename(path)
                elc = input(f"¿Estas seguro de que quieres abrir {archivo}?\n1)Si\n2)No\nEleccion: ")
                try:
                    elc = int(elc)
                except:
                    print("Debes ingresar un numero! Vuelve a empezar.")
                    input("Presione enter para continuar..")
                    os.system("cls")
                    continue
                if elc == 1 or elc == 2: 
                    if elc == 1:
                            archivo = open(path, "r")
                            for line in archivo:
                                line.rstrip()
                                print(line)
                                input("Presione enter para continuar...")
                    if elc == 2:
                        input("Presione enter para continuar..")
                        os.system("cls")
                        continue  
                else:
                    print("No se ha entendido tu eleccion")
                    input("Presione enter para continuar...")
                    continue
            if elc == 3:
                elc = input(f"{colors.BOLD}{colors.WARNING}¿Confirmas que quieres salir?{colors.ENDC}\n1)Si\n2)No\nEleccion: ")
                try:
                    elc = int(elc)
                except:
                    print("Inserta un numero!")
                    input("Inserte enter para continuar..")
                    os.system("cls")
                if elc == 1 or elc == 2:
                    if elc == 1:
                        break
                    if elc == 2:
                        os.system("cls")
                        continue
                else: 
                    print("No se entiende tu eleccion.")
                    input("Presione enter para continuar..")
                    os.system("cls")
                    continue
        else:
            print("No se entendio tu eleccion..")
            input("Presione enter para continuar...")
            os.system("cls")
        
def filtrar ():
    contador = 0
    archivo = input("Inserta la ruta del archivo que deseas filtrar: ")
    if os.path.exists(archivo) == True:
        os.chdir(archivo)
        os.system("cls")
        print("Ubicacion:", os.getcwd())
        name = input("Inserta el nombre exacto del archivo: ")
        archivo = open(name, "r")
        elc = input(f"{colors.BOLD}¿Que deseas encontrar?{colors.ENDC}\n1)¿Cuantos renglones empiezan con esta palabra?\n2)¿Cuantos renglones contienen esta palabra?\nEleccion: ")
        try:
            elc = int(elc)
        except:
            print("Debes insertar un numero.")
            input("Inserta enter para continuar..")
            os.system("cls")
        if 1 <= elc <= 2:
            if elc == 1:
                word = input("Filtro: ")
                for linea in archivo:
                    if linea.startswith(word):
                        contador += 1
                print(f"El documento empieza {contador} veces con {word} ")
                input("Inserte enter para continuar...")
                os.system("cls")
            if elc == 2:
                word = input("Filtro: ")
                for linea in archivo:
                    if word in linea:
                        contador += 1
                print(f"El documento tiene {contador} lineas con {word} ")
                input("Inserte enter para continuar...")
                os.system("cls")
        else:
            print("No se entiende tu eleccion.")
            input("Presione enter para continuar..")
            os.system("cls")
    else:
        print("No existe tal ruta...")
        input("Presione enter para continuar...")
        os.system("cls")
    
def rename():
    print('''Para este modo, debes tener en cuenta que para cambiar el nombre debes hacer lo siguiente:
          Inserta ruta del archivo: /home/decodigo/Documentos/python/archivos/archivo.txt
          Inserta nuevo nombre del archivo: /home/decodigo/Documentos/python/archivos/archivo_renombrado.txt
        
          Basicamente, debes cambiar "archivo.txt" por el nombre que quieras, por ejemplo "archivo_renombrado.txt"
          ''')
    input("Presione enter para continuar...")
    os.system("cls")
    path = input("Inserta ruta del archivo: ")
    name = input("Inserta nuevo nombre del archivo:  ")
    os.rename(path, name)
    input("Se ha completado con exito!")
    os.system("cls")
    
def delete():
    while True:
        os.system("cls")
        elc = input(f"{colors.BOLD}Elija una de las siguientes opciones:{colors.ENDC}\n1)Eliminar archivo\n2)Eliminar carpeta\n3)Salir\nEleccion: ")
        try:
            elc = int(elc)
        except:
            print("Inserta un numero!")
            input("Inserte enter para continuar..")
            os.system("cls")
            continue
        if 1 <= elc <= 3:
            if elc == 1:
                path = input("Inserte ruta del archivo: ")
                if os.path.exists(path) == True:
                    elc = input(f"{colors.BOLD}{colors.WARNING}Estas seguro de eliminar la ruta?{colors.ENDC}\n1)Si\n2)No\nEleccion: ")
                    try:
                        elc = int(elc)
                    except:
                        print("Debes insertar un numero")
                        input("Inserte enter para continuar..")
                        os.system("cls")
                    if elc == 1 or elc == 2:
                        if elc == 1:
                            os.remove(path)
                            input("Se ha eliminado con exito!")
                            os.system("cls")
                            break
                        if elc == 2:
                            os.system("cls")
                            continue
                    else:
                        input("No se ha entendido, inserte enter para continuar")
                        continue      
                else:
                    print("No existe esa ruta")
                    input("Inserte enter para continuar..")
                    os.system("cls")
                    continue
            if elc == 2:
                elc = input(f"{colors.BOLD}Inserte una de las dos opciones:{colors.ENDC}\n1)Es una carpeta con archivos\n2)Carpete Vacia\nEleccion: ")
                try:
                    elc = int(elc)
                except:
                    print("Debes insertar un numero")
                    input("Inserte enter para continuar..")
                    os.system("cls")
                if elc == 1 or elc == 2:
                    if elc == 1:
                        path = input("Inserte ruta de la carpeta:")
                        if os.path.exists(path) == True:
                            elc = input(f"{colors.BOLD}{colors.WARNING}Estas seguro de eliminar la ruta {colors.ENDC}\n1)Si\n2)No\nEleccion: ")
                            try:
                                elc = int(elc)
                            except:
                                print("Debes insertar un numero")
                                input("Inserte enter para continuar..")
                                os.system("cls")
                            if elc == 1 or elc == 2:
                                if elc == 1:
                                    rmdir(path)
                                    input("Se ha eliminado con exito!")
                                if elc == 2:
                                    input("Inserte enter para continuar...")
                                    os.system("cls")
                                    continue
                            else:
                                input("No se ha entendido, inserte enter para continuar")
                                continue
                        else:
                            print("No existe esa ruta")
                            input("Inserte enter para continuar..")
                            os.system("cls")
                            continue
                    if elc == 2:
                        path = input("Inserte ruta de la carpeta:")
                    if os.path.exists(path) == True:
                        elc = input(f"{colors.BOLD}{colors.WARNING}Estas seguro de eliminar la ruta?{colors.ENDC}\n1)Si\n2)No\nEleccion: ")
                        try:
                            elc = int(elc)
                        except:
                            print("Debes insertar un numero")
                            input("Inserte enter para continuar..")
                            os.system("cls")
                        if elc == 1 or elc == 2:
                            if elc == 1:
                                rmdir(path)
                                input("Se ha eliminado con exito!")
                            if elc == 2:
                                input("Presione enter para continuar...")
                                os.system("cls")
                                continue
                        else:
                            input("No se ha entendido, inserte enter para continuar")
                            continue
                    else:
                        print("No existe esa ruta")
                        input("Inserte enter para continuar..")
                        os.system("cls")
                        continue
                else:
                    input('''No se ha entendido la eleccion
                             Inserte enter para continuar..''')
                    continue
            if elc == 3:
                elc = input(f"{colors.BOLD}{colors.WARNING}¿Confirmas que quieres salir?{colors.ENDC}\n1)Si\n2)No\nEleccion: ")
                try:
                    elc = int(elc)
                except:
                    print("Inserta un numero!")
                    input("Inserte enter para continuar..")
                    os.system("cls")
                if elc == 1 or elc == 2:
                    if elc == 1:
                        os.system("cls")
                        break
                    if elc == 2:
                        os.system("cls")
                        continue
                else:
                    input("No se ha entendido, inserte enter para continuar")
                    continue
                    
        else:
            input("No se entendio tu eleccion...")
            os.system("cls")
            continue

def main():
    os.system("cls")
    while True:
        menu()
        elc = input("Inserta tu eleccion: ")
        try:
            elc = int(elc)
        except:
            print("Debes insertar un numero")
            input("Inserte enter para continuar..")
            os.system("cls")
        if 1 <= elc <= 8:
            if elc == 1:
                carpeta()
            if elc == 2:
                ubicacion()
            if elc == 3:
                tamanio()
            if elc == 4:
                cambiar_ubi()
            if elc == 5:
                archivo()
            if elc == 6:
                filtrar()
            if elc == 7:
                rename()
            if elc == 8:
                delete()
        else:
            input("No se entendio tu eleccion...")
            os.system("cls")
            continue
        
if __name__ == "__main__":
    main()
        

      