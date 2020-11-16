#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


import csv
import re

# Creo una funcion para sacar el tiempo y usarlo en el programa
def calculos_segundos(data,i,keys):
    valor = data[i].get(keys)
    try:
        dividir = valor.split(sep=":")
        hora = int(dividir[0])
        minutos = int(dividir[1])
        segundos = int(dividir[2])
        segundos_totales = hora * 3600 + minutos * 60 + segundos 
        return segundos_totales
    except:
        pass
  

def ironman():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
    # Abro archivo
    with open('2019_ironman.csv') as csvfile:
        data = list(csv.DictReader(csvfile))

    # Cargo Varibles necesarias
    cantidad_filas = len(data)
    mpro_maximo_swim = 0
    mpro_minimo_swim = 0
    mpro_maximo_bike = 0
    mpro_minimo_bike = 0
    mpro_maximo_run = 0
    mpro_minimo_run = 0
    sumatoria_swim = 0
    sumatoria_bike = 0
    sumatoria_run = 0
    total = 0
    conteo1 = 0
    conteo2 = 0
    conteo3 = 0

    # Creo un Bucle sacando la info de las 3 categorias
    for i in range(cantidad_filas):
        row = data[i]
        division = str(row.get("Division"))
        if division == "MPRO":
                keys = "Swim"
                total = calculos_segundos(data,i,keys)
                try:
                    if (mpro_maximo_swim == 0) or (total > mpro_maximo_swim):
                        mpro_maximo_swim = total
                    if (mpro_minimo_swim == 0) or (total < mpro_minimo_swim):
                        mpro_minimo_swim = total
                    sumatoria_swim += total
                    conteo1 += 1
                except:
                    pass
                keys = "Bike"
                total = calculos_segundos(data,i,keys)
                try:
                    if (mpro_maximo_bike == 0) or (total > mpro_maximo_bike):
                        mpro_maximo_bike = total
                    if (mpro_minimo_bike == 0) or (total < mpro_minimo_bike):
                        mpro_minimo_bike = total
                    sumatoria_bike += total
                    conteo2 += 1
                except:
                    pass
                keys = "Run"
                total = calculos_segundos(data,i,keys)
                try:
                    if (mpro_maximo_run == 0) or (total > mpro_maximo_run):
                        mpro_maximo_run = total
                    if (mpro_minimo_run == 0) or (total < mpro_minimo_run):
                        mpro_minimo_run = total
                    sumatoria_run += total
                    conteo3 += 1
                except:
                    pass
    
    # Calculo el promedio y lo almaceno.
    promedio = sumatoria_swim / conteo1
    promedio1 = sumatoria_bike / conteo2
    promedio2 = sumatoria_run / conteo3

    # Imprimo resultados
    print("El Tiempo MAXIMO de Swim fue:",mpro_maximo_swim)
    print("El Tiempo MINIMO de Swim fue:",mpro_minimo_swim)
    print("El PROMEDIO de Swim fue",promedio)
    print("El Tiempo MAXIMO de Bike fue",mpro_maximo_bike)
    print("El Tiempo MINIMO de Bike fue",mpro_minimo_bike)
    print("El PROMEDIO de bike fue",promedio1)
    print("El Tiempo MAXIMO de Run fue",mpro_maximo_run)
    print("El Tiempo MINIMO de Run fue",mpro_minimo_run)
    print("El PROMEDIO de Run fue",promedio2)




    

if __name__ == '__main__':
    print("Ejercicios de práctica extra")
    ironman()
