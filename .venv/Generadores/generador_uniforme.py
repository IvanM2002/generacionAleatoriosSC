import random
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

# Parámetros del generador lineal congruencial
a = 1664525                         #Pendiente  = {a E Z | 1 <= a < m}
c = 1013904223                      #Intersección = {c E Z | 0 <= C < m} 
m = 2**32                           #Conjunto = {m E Z | m > 0} 
ri = []                             #Numeros Ri
ni = []                             #Numeros Ni

# FUNCIÓN PARA GENERAR RI CON CONGRUENCIA LINEAL
def generar_ri(semilla,total):   
    ri.clear()
    if semilla is None:
        semilla = random.randint(0, m - 1)  #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m} se utiliza unicamente para generar una semilla si no se especifica una
        
    for _ in range(total):
        semilla = (a * semilla + c) % m
        ri.append(semilla / (m - 1))                  
        
        
#FUNCIÓN PARA GENERAR NI CON DISTRIBUCION UNIFORME
#Intervalo superior (maxI)
#Intervalo Inferior (minI)
def generarDistrUniforme(maxIntervalo,minIntervalo,semilla,total):
    global ni
    ni = []   
    generar_ri(semilla,total)
    ni += [(minIntervalo + (maxIntervalo - minIntervalo) * N) for N in ri]    
    return ni      

#Numero de intervalos para la grafica (nuIntervalos)
def generar_histograma(num_intervalos,minI,maxI):
    """Genera un histograma de frecuencia por intervalo."""
    # Calcular los intervalos
    intervalos = np.linspace(minI, maxI, num=num_intervalos+1)
    
    frecuencia, bordes = np.histogram(ni, bins=intervalos)
        
    plt.bar(range(len(frecuencia)), frecuencia, edgecolor='black')
    
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Frecuencia por Intervalo')
    
    plt.show()

def guardar_en_csv(nombre_archivo='distribucionUniforme.csv'):
    # Comprobar si la carpeta CSVs existe, si no, crearla
    carpeta_csv = 'CSVs'
    if not os.path.exists(carpeta_csv):
        os.makedirs(carpeta_csv)

    ruta_archivo = os.path.join(carpeta_csv, nombre_archivo)

    with open(ruta_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['pseudoaleatorios'])
        escritor_csv.writerows(map(lambda x: [x], ni))         