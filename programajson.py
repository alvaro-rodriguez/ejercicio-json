#!/usr/bin/python
# -*- coding: utf-8 -*-

#"Pre-Enunciado"

"""
1.Cuenta los títlos de los distintos elementos .

2.Lista los distintos elementos (Resoluciones,Edictos,Anuncios,etc) y la cantidad de cada uno.

3.Pide un tipo de elemento( Resoluciones,Edictos,Anuncios,etc) y te muestra todos los que son del mismo tipo junto con la fecha de emisión, el organismo emisor ,la sección a la que pertenecen y la página en la que empieza.

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
    print "|  -Imprime los datos en formato html - 5                           |"              
    print "|                                                                   |"
    print "| número de elementos actuales: %i                               |" % (len(doc))
    print "|(Para salir usar la letra 'q')                                     |"
    print "+-------------------------------------------------------------------+"
    respuesta = raw_input("respuesta: ")

    #Comprobador de respuesta
    if respuesta == "q":
        salir = True
    
    elif respuesta == "1":
        os.system('clear')
        print "+-------------------------------+"
        print "| Cuenta cada tipo de elemento. |"
        print "+-------------------------------+"
        tipos = {}
        print "+----------------------------+-------------"
        print "|Nombre del Artículo         |Cantidad" 
        for d in doc :
            #Las opciones comentadas sirven para testear el funcionamiento del programa.

            if d['Tipo'] not in tipos:
                tipos[d['Tipo']] = 1
                #print "Se ha encontrado un nuevo tipo"

            elif d['Tipo'] in tipos:
                tipos[d['Tipo']] = tipos[d['Tipo']] + 1
                #print "se ha añadido uno"

            #else:
                #print "FAIL"

        for t in tipos:
            print"|" ,t , tipos[t]
        print "+-------------------------------------------"    
        raw_input("Pulse enter para continuar")
            
    elif respuesta == "2":
        os.system('clear')
        print "+-----------------------------+"
        print "| Buscador de artículos.      |"
        print "+-----------------------------+"
        """3.Pide un tipo de elemento( Resoluciones,Edictos,Anuncios,etc) y te muestra todos los que son del mismo tipo junto con la fecha de emisión, el organismo emisor ,la sección a la que pertenecen y la página en la que empieza."""
        print "Indique el tipo de artículo sobre el que quiere buscar."
        arti = raw_input("Tipo: ")
        artfa = False
        for d in doc :
            if d['Tipo'] == arti:
                print "+-----------------------------------------------"
                print "|id:",d['id'] 
                print "|Fecha de disposición: ",d['FechaDisposicion']
                print "|Organismo emisor: " , d['OrganismoEmisor']
                print "|Sección: ",d['Seccion']
                print "|Abarca desde la página %i a la página %i" % (d['PaginaInicial'],d['PaginaFinal'])
                artfa = True
        if artfa == False:
            print "No se ha encontrado  ningún artículo que coincida."
        else:
        
            print "+-----------------------------------------------"
        raw_input("Pulse enter para continuar")

    elif respuesta == "3":
        os.system('clear')
        print "+-----------------------------------+"
        print "| Buscador de elementos por fecha.  |"
        print "+-----------------------------------+"
        print "Busca artículos que puedan haber sido publicadosen la fecha que indique."
        print "La fecha deberá llevar el siguiente formato: 'DD/MM/YYYY'"
        fecha = raw_input("Introduzca la fecha: ")
        fecok = False
        for d in doc:
            if fecha == d['FechaBOJA']:
                fecok = True
                print "id:",d['id'],"Tipo de artículo:",d['Tipo']
                print "Abarca desde la página %i a la página %i" % (d['PaginaInicial'],d['PaginaFinal'])
                
                

        if fecok == False:
            print "No se ha encontrado ningún artículo que coincida con esa fecha."
            
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
                print "|Número de BOJA: ",d['NumeroBOJA'] ,"Tipo de artículo: " ,d['Tipo']
                print "Organismo emisor: ", d['OrganismoEmisor']
                print "|Fecha de disposición: ",d['FechaDisposicion']
                print "|id del artículo: ",d['id'],"Sección: ",d['Seccion']
                print "+---------------------------------------------------------+"
                print d['Sumario']
                print "+---------------------------------------------------------+"
        raw_input("Pulse enter para continuar")
        
    elif respuesta == "5":
        os.system('clear')
        print "+-------------------------------+"
        print "| Función de impresión en html. |"
        print "+-------------------------------+"
        
        print "Imprime todas las publicaciones."
        raw_input("Pulse enter para Mostrar los resultados")        
        for d in doc :
            print "<h1>",d['Tipo'],"</h1>"
            print "<p>",d['Sumario'],"</p>"
            print "<a href='",d['url'],"'>","Más información","</a>"

        print "Si desea guardad estos datos en un fichero escriba 'yes'."
        resp3 = raw_input("¿Escribir datos? ")
        if resp3 == "yes":
            fichero = open(index.html,"r+")
            for h in hojas:
                fichero.write("<h1>"+d['Tipo']+"</h1>"+"\n")
                fichero.write("<p>"+d['Sumario']+"</p>"+"\n")
                fichero.write("<a href='"+d['url']+"'>"+"Más información"+"</a>"+"\n")

        raw_input("Pulse enter para continuar")
 
            

