#!/usr/bin/python
# -*- coding: utf-8 -*-

#"Pre-Enunciado"

"""
1.Cuenta los títlos de los distintos elementos .

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
    print "+-------------------------------------------------------------------+"
    print "| Consultor del BOJA.                                               |"
    print "|                                                                   |"
    print "|  Opciones disponibles:                                            |"
    print "|  -Muestra la cantidad de cada tipo de elemento. - 1               |"
    print "|  -Muestra información sobre el tipo de elemento relacionado. - 2  |"
    print "|  -Muestra todos los elementos 'hechos en na fecha'. - 3           |"
    print "|  -Muestra la información completa de una página.  - 4             |"
    print "|  -\\\Mostrar el contenido del archivo/// -> z                     |"
    print "|                                                                   |"
    print "| número de elementos actuales: %i                               |" % (len(doc))
    print "|(Para salir usar la letra 'q')                                     |"
    print "+-------------------------------------------------------------------+"
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
        

    elif respuesta == "1":
        os.system('clear')
        print "+-----------------------------+"
        print "| Cantidad de cada elemento.  |"
        print "+-----------------------------+"
                
        raw_input("Pulse enter para continuar")

    elif respuesta == "2":
        os.system('clear')
        print "+-----------------------------+"
        print "| Cantidad de cada elemento.  |"
        print "+-----------------------------+"
                
        raw_input("Pulse enter para continuar")

    elif respuesta == "3":
        os.system('clear')
        print "+-----------------------------+"
        print "| Cantidad de cada elemento.  |"
        print "+-----------------------------+"
                
        raw_input("Pulse enter para continuar")

        
    elif respuesta == "4":
        os.system('clear')
        print "+-------------------------------------+"
        print "| Consultor de página del BOJA.       |"
        print "+-------------------------------------+"
        nmpa = 0
        for d in doc :
            if d['PaginaFinal'] > nmpa: 
                nmpa =  d['PaginaInicial']
                    
        print "El número actual de páginas es :" ,nmpa
        print "Elija en número de página que quiere consultar "
        npa = int(raw_input("número de página:"))
        for d in doc:
            if npa == d['PaginaInicial']:
                print "+---------------------------------------------------------+"
                print "|Página Inicial: " ,d['PaginaInicial']," Página final: ",d['PaginaFinal']
                print "|Número de BOJA: ",d['NumeroBOJA'] ,"Tipo de artículo: " ,d['Tipo'],"Organismo emisor: ", d['OrganismoEmisor']
                print "|Fecha de disposición: ",d['FechaDisposicion']
                print "|id del artículo: ",d['id'],"Sección: ",d['Seccion']
                print "-----------------------------------------------------------"
                print d['Sumario']
                print "+---------------------------------------------------------+"
        raw_input("Pulse enter para continuar")
        

 
            

