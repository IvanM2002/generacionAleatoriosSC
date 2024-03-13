from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

numeros_generados = []


def congruencia_lineal(semilla, a, c, m, n):
    numeros_generados.clear()
    for _ in range(n):
        semilla = (a * semilla + c) % m
        numeros_generados.append(semilla / (m - 1))
    return numeros_generados


def congruencia_lineal_range(semilla, a, c, m, n, min, max):
    numeros = congruencia_lineal(semilla, a, c, m, n).copy();
    numeros_generados.clear()
    for numero in numeros:
        numeros_generados.append((int)(numero * ((max - min) + 1) + min))
    return numeros_generados


def generar_grafica():
    # Definir los intervalos para el histograma
    bins = np.arange(min(numeros_generados), max(numeros_generados) + 0.1, 0.1)

    # Crear el histograma
    plt.hist(numeros_generados, bins=bins, edgecolor='black')

    # Configurar etiquetas y título
    plt.xlabel('Valor Inverso')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Frecuencia para Valores')

    # Mostrar el histograma
    plt.show()

def guardar_en_csv(nombre_archivo='congruencia_lineal.csv'):
    # Comprobar si la carpeta CSVs existe, si no, crearla
    carpeta_csv = 'CSVs'
    if not os.path.exists(carpeta_csv):
        os.makedirs(carpeta_csv)

    ruta_archivo = os.path.join(carpeta_csv, nombre_archivo)

    with open(ruta_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['pseudoaleatorios'])
        escritor_csv.writerows(map(lambda x: [x], numeros_generados))


semilla = 1  # Semilla inicial
a = 9  # pendiente
c = 3  # Intercepto
m = 128  # campo numerico
n = 10  # Cantidad de números aleatorios a generar
numeros_aleatorios = congruencia_lineal_range(semilla, a, c, m, n, min=10, max=15)
print(congruencia_lineal_range(semilla, a, c, m, n, min=10, max=15))
generar_grafica()
