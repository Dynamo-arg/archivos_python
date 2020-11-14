#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import csv
import re

def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    fi = open('texto.txt', 'r')
    lineas = 0
    for line in fi:
        largo = len(line)
        cantidad_letras += largo
        lineas += 1
    print("Este Archivo contiene", lineas , "Total caracteres", cantidad_letras)
    fi.close()


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    fo = open("ingreso.txt", "w")
    bucle = 1
    while bucle != 0:
        texto = str(input("Ingrese texto para Añadir para terminar ENTER\n"))
        texto_salto = (texto,"\n")
        fo.writelines(texto_salto)
        bucle = len(texto)
        if bucle == 0:
            break
        else:
            cantidad_letras += bucle     
    print("Cantidad de letras ingresadas:", cantidad_letras)
    fo.close()
    




def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    cantidad_ambientes = int(input("Ingrese la cantidad de Ambientes solicitados:\n"))
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    # Cargo las variables:
    cantidad_filas = len(data)
    moneda_pesos = 0
    valor_alquiler = 0
    valor_maximo = 0
    valor_minimo = 0
    # Empiezo Bucle para sacar toda la info solicitada
    for i in range(cantidad_filas):
        # Agrege esta linea porque algunas lineas no tenian datos y daba error!
        if data[i].get('ambientes') != "":
            if cantidad_ambientes == int(data[i].get('ambientes')):
                if data[i].get('moneda') == "ARS":
                    moneda_pesos +=1
                    valor_alquiler += float(data[i].get('precio'))
                    if valor_maximo < float(data[i].get('precio')):
                        valor_maximo = float(data[i].get('precio'))
                    if (valor_minimo == 0) or (valor_minimo > float(data[i].get('precio'))):
                        valor_minimo = float(data[i].get('precio'))
  

    promedio = valor_alquiler / moneda_pesos
    print("Deptos de", cantidad_ambientes, "Hay en alquileres en pesos", moneda_pesos)
    print("El promedio de estos departamentos son:", promedio)
    print("valor maximo", valor_maximo)
    print("valor minimo", valor_minimo)





if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    ej3()
