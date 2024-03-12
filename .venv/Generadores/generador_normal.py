import random
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import csv

# Parámetros del generador lineal congruencial
a = 1664525                         #Pendiente  = {a E Z | 1 <= a < m}
c = 1013904223                      #Intersección = {c E Z | 0 <= C < m} 
m = 2**32                           #Conjunto = {m E Z | m > 0} 
semilla = 1                         #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m}
ri = []                             #Numeros Ri


# Lista de números pseudoaleatorios de convolución
numeros_pseudoaleatoriosMedDes = [15.68866392,17.08559662,17.15452055,15.15261532,17.63585243,17.10922827,16.64418793,
                                  16.83252325,15.46909741,17.43582994,15.87918557,16.04895496,16.12241714,17.51470964,17.89848077,]

# Parámetros de la distribución normal
media = np.mean(numeros_pseudoaleatoriosMedDes)
desviacion_estandar = np.std(numeros_pseudoaleatoriosMedDes)
ni = []                                                             #Numeros Ni


# Función para generar Ri con congruencia Lineal
def generar_ri(semilla,n):   
    
    if semilla is None:
        semilla = random.randint(0, m - 1)  #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m} se utiliza unicamente para generar una semilla si no se especifica una
        
    for _ in range(n):
        semilla = (a * semilla + c) % m
        ri.append(semilla / (m - 1))    


def generarDistrNormal(semilla,n):
    global ni
    generar_ri(semilla,n)
    ni += [norm.ppf(numero, loc=media, scale=desviacion_estandar) for numero in ri]
    # Calcular la inversa de la distribución normal para cada número pseudoaleatorio
    return ni

def generar_grafica():        

    # Definir los intervalos para el histograma
    bins = np.arange(min(ni), max(ni) + 0.1, 0.1)

    # Crear el histograma
    plt.hist(ni, bins=bins, edgecolor='black')

    # Configurar etiquetas y título
    plt.xlabel('Valor Inverso (ni)')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Frecuencia para Valores Inversos')

    # Mostrar el histograma
    plt.show()
    
def guardar_en_csv(nombre_archivo='distribucionNormal.csv'):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['pseudoaleatorios'])
        escritor_csv.writerows(map(lambda x: [x], ni))    


generarDistrNormal(semilla,50000)
generar_grafica()
