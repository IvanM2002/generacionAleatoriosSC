import random
import matplotlib.pyplot as plt
import numpy as np
import csv

# Parámetros del generador con distribucion Uniforme 
maxI = 10                            #Intervalo superior
minI = 0                             #Intervalo Inferior
ni = []                              #Numeros Ni
nuIntervalos = 8                     #Numero de intervalos para la grafica

# Parámetros del generador lineal congruencial
a = 1664525                         #Pendiente  = {a E Z | 1 <= a < m}
c = 1013904223                      #Intersección = {c E Z | 0 <= C < m} 
m = 2**32                           #Conjunto = {m E Z | m > 0} 
semilla = 10                         #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m}
ri = []                             #Numeros Ri


# Función para generar Ri con congruencia Lineal
def generar_ri(semilla,total):   
    
    if semilla is None:
        semilla = random.randint(0, m - 1)  #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m} se utiliza unicamente para generar una semilla si no se especifica una
        
    for _ in range(total):
        semilla = (a * semilla + c) % m
        ri.append(semilla / (m - 1))                  
        
        
# Función para generar Ni con distribucion Uniforme
def generarDistrUniforme(ri, maxIntervalo,minIntervalo,semilla,total):
    global ni
    generar_ri(semilla,total)
    ni += [(minIntervalo + (maxIntervalo - minIntervalo) * N) for N in ri]
    return ni 
    

def generar_histograma(num_intervalos):
    """Genera un histograma de frecuencia por intervalo."""
    # Calcular los intervalos
    intervalos = np.linspace(minI, maxI, num=num_intervalos+1)

    # Crear histograma de frecuencia
    frecuencia, bordes = np.histogram(ni, bins=intervalos)

    # Imprimir los resultados
    print("Intervalos:", bordes)
    print("Frecuencia en cada intervalo:", frecuencia)

    # Crear el gráfico de barras
    plt.bar(range(len(frecuencia)), frecuencia, edgecolor='black')

    # Etiquetas y título del gráfico
    plt.xlabel('Intervalos')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Frecuencia por Intervalo')

    # Mostrar el gráfico
    plt.show()
    
def guardar_en_csv(nombre_archivo='distribucionUniforme.csv'):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['pseudoaleatorios'])
        escritor_csv.writerows(map(lambda x: [x], ni))        
    
    
generarDistrUniforme(ri,maxI,minI,semilla,10000)
generar_histograma(nuIntervalos)