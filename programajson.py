#!/usr/bin/python
# -*- coding: utf-8 -*-

#"Pre-Enunciado"

"""
1.Lista cuenta los títlos de los distintos elementos .

2.Lista los distintos elementos (Resoluciones,Edictos,Anuncios,etc) y la cantidad de cada uno.

3.Pide un tipo de elemento( Resoluciones,Edictos,Anuncios,etc) y temuestra todos los que son del mismo tipo junto con la fecha de emisión, el organismo emisor ,la sección a la que pertenecen y la página en la que empieza.

4.Pide una fecha y muestra todos los elementos que se han emitido en la misma .

5.Pide un número de página y te muestra  toda la información referente (tipo,"url",fecha de emisión,sección y sumario) a los edictos, anuncios ,etc que se encuentran en ella 
"""

#importación de librerías
#import xpath
import os
import json
from pprint import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf8')


#Carga el fichero xml en una variable
with open('ficheroson.json') as datos:
    doc = json.load(datos)



#Bucle del programa
salir = False

while salir == False:
    os.system('clear')
    print "+----------------------------------------------------------+"
    print "| Consultor del BOJA.                                      |"
    print "|                                                          |"
    print "|  Opciones disponibles:                                   |"
    print "|  -Conteo de partidos - 1                                 |"
    print "|  -Número de electos por partido - 2                      |"
    print "|  -Datos concretos de un partido - 3                      |"
    print "|  -Buscador por número de electos  - 4                    |"
    print "|  -Otros datos - 5                                        |"
    print "|  -\\\Mostrar el contenido del archivo/// -> z            |"
    print "|                                                          |"
    print "|(Para salir usar la letra 'q')                            |"
    print "+----------------------------------------------------------+"
    respuesta = raw_input("respuesta: ")

    #Comprobador de respuesta
    if respuesta == "q":
        salir = True

    elif respuesta == "z":
        os.system('clear')
        print "+-----------------------------+"
        print "| Conteo de partidos.         |"
        print "+-----------------------------+"
        for d in doc :
            print d['Tipo']
            print d['FechaBOJA']
        raw_input("Pulse enter para continuar")
        
"""
    elif respuesta == "1":
        os.system('clear')
        print "+-----------------------------+"
        print "| Conteo de partidos.         |"
        print "+-----------------------------+"
        raw_input("Pulse enter para continuar")

        


    elif respuesta == "2":
        os.system('clear')
        print "+--------------------------------+"
        print "| Número de electos por partido. |"
        print "+--------------------------------+"
        raw_input("Pulse enter para continuar")




    elif respuesta == "3":
        os.system('clear')
        print "+----------------------------------------+"
        print "| Datos concretos de un partido.         |"
        print "+----------------------------------------+"
        print "Introduzca el nombre del partido sobre le que desea buscar:"
        raw_input("Pulse enter para continuar")

 


    elif respuesta == "4":
        os.system('clear')
        print "+-------------------------------------+"
        print "| Buscador por número de electos      |"
        print "+-------------------------------------+"
        raw_input("Pulse enter para continuar")


    elif respuesta == "5":
        os.system('clear')
        print "+------------------------------------+"
        print "| Otros datos.                       |"
        print "| -Datos generales de la encuesta -1 |"
        print "| -Gráficos de las elecciones -2     |"
        print "+------------------------------------+"

        raw_input("Pulse enter para continuar")

        elif resp2 == "2":
            os.system('clear')
            print "+----------------------------------+"
            print "|   Gráficos de las elecciones     |"
            print "+----------------------------------+"
            
            raw_input("Pulse enter para continuar")
            
"""
