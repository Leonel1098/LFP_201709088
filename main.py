from tkinter import filedialog
from tkinter import Tk
import os
from Pelicula import *
lista_peliculas = []

"\n"
opcion = input("Lenguajes Formales y de Programación\nSección : B+ \nCarnet : 201709088 \nNombre : Leonel Antonio González García\n")
print("            Bienvenido  ")

def Menu(): 
    while True:
        print("------------------------------------------------------")
        
        print(">->->->->->->->MENÚ<-<-<-<-<-<-<-<")
        print(" 1. Cargar Archivo")
        print(" 2. Gestionar Películas")
        print(" 3. Filtrar")
        print(" 4. Gráfica")
        print(" 5. Salir")
        print("-------------------------------------------------------")
        # solicituamos una opción al usuario
        opcionMenu = input(" Por favor seleccione una opcion >> ")
        
        if opcionMenu =="1":
           print("---->Cargar Archivo de Entrada")
           print("")
           CargarArchivo()
           

        elif opcionMenu =="2":
            print("---->Gestionar Películas")
            clear()
            MenuGestionar()
            print("")
            
            
        elif opcionMenu =="3":
            print("----->Filtrar")
            clear()
            MenuFiltrar()
            print("")
            
        elif opcionMenu =="4":
            print("----->Gráfica ")
            print("")

        elif opcionMenu=="5":
            print("Adios Goku")
            break
        else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\n Pulsa una tecla para continuar")
        
def MenuGestionar():
     while True:
        print("")
        print(".............MENÚ GESTIONAR.............")
        print("     a. Mostrar Películas")
        print("     b. Mostrar Actores")
        print("     c. Regresar a Menú")
        print("")
        # solicituamos una opción al usuario
        opcionMenu = input(" Por favor seleccione una opcion >> ")
        
        if opcionMenu =="a":
           print("  ---->Mostrar Películas")
           print("")
           mostrarPeliculas()
        elif opcionMenu =="b":
            print(" ---->Mostar Actores")
            print("")
            
        elif opcionMenu=="c":
            clear()
            break
            
        else:
                    print ("")
                    input("No has pulsado ninguna opción correcta...\n Pulsa una tecla para continuar")
def MenuFiltrar():
     while True:
        print("")
        print(".............MENÚ FILTRAR.............")
        print("     a. Filtrar por Actor")
        print("     b. Filtrar por Año")
        print("     c. Filtrar por Género")
        print("     d. Regresar a Menú ")
        print("")
        # solicitamos una opción al usuario
        opcionMenu = input(" Por favor seleccione una opcion >> ")
        
        if opcionMenu =="a":
           print("  ---->Filtrar por Actor")
           print("")

        elif opcionMenu =="b":
            print(" ---->Filtrar por Año")
            print("")

        elif opcionMenu =="c":
            print(" ---->Filtrar por Género")
            print("")
        elif opcionMenu=="d":
            clear()
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\n Pulsa una tecla para continuar")

#Método para cargar el archivo mediante un administrador de archivos
def CargarArchivo():
        root = Tk()

        #Abre Ventana para Buscar el archivo .lfp 
        archivo =  filedialog.askopenfilename(initialdir = "/") 
        
        #Abre el achivo 
        archivo_texto = open(archivo ,'r',encoding="utf8")
        
        #Contenido del archivo leido 
        texto = archivo_texto.read()
        archivo_texto.close()

        #Analiza el contenido del Archivo 
        global Data
        Data = texto
        root.destroy()
        print(Data)
        print("Carga Exitosa")
        diccionario()
       
    
def diccionario():
    info = Data.split("\n")
    for s in info:
        diccionario = s.split(";")

        peli = {
            "nombre:" +diccionario[0],
            "reparto:" +diccionario[1],
            "año:" +diccionario[2],
            "genero:"+diccionario[3]
        }
        lista_peliculas.append(peli)
    print(lista_peliculas)

#Método que muestra las películas del archivo cargado   
def mostrarPeliculas():
    print(lista_peliculas)
    info = Data.split("\n")

    for s in info:
        diccionario = s.split(";")
        print("------------------Película-----------------")
        print("nombre:"+diccionario[0])
        print("Reparto:"+diccionario[1])
        print("año:"+diccionario[2])
        print("Genero:"+diccionario[3])

#Método para limpiar la consola  
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
     

Menu()
 ###for i in leer: 
             ###nombre, actores,año,genero = i[0],i[1],i[2],i[3]
             ###variable1 = Pelicula(nombre, actores, año, genero)
             ###arreglo.append(variable1)

###for i in range(len(arreglo)):
             ###print(arreglo[i].getNombre())
        
        ###arreglo[0].setNombre("Nombre") 
        ###for i in range(len(arreglo)):
             ###print(arreglo[i].getNombre())

       ###print(arreglo[2].getActor())


   ### print("buscar por id del atributo del diccionario  lista------------------------------")
    ###print(pelis[0]["nombre"])
   ### print("--------------------------para Recorere")
    ###for p in pelis:
   ### print(p["nombre"])###

   ###d= data.split("\n")
###for s in d:
    ###d2 = s.split(";")
    ###print("------------------Pelicula-----------------")
    ###print("nombre:"+d2[0])
    ###print("Reparto:"+d2[1])
    ###print("año:"+d2[2])
    ###print("Genero:"+d2[3])