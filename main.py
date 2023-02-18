from tkinter import filedialog
import os

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
        

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def CargarArchivo():
        print("Boton Cargar Archivo")

        
        #Abre Ventana para Buscar el archivo .lfp 
        archivo =  filedialog.askopenfilename(initialdir = "/") 
            #Abre el achivo 
        archivo_texto = open(archivo ,'r',encoding="utf8")
            #Contenido del archivo leido 
        texto = archivo_texto.read()
        archivo_texto.close()
            #Analiza el contenido del Archivo 
        
        global Instrucciones
        Instrucciones = texto
        
       
        print(Instrucciones)

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
        # solicituamos una opción al usuario
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
     

Menu()