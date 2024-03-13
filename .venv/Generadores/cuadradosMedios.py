from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
import csv
import os


numeros_generados = []
def cuadrados_medios(semilla, n):
    numeros_generados.clear()
    for _ in range(n):
        semilla = int(str(semilla ** 2).zfill(8)[2:6])
        numeros_generados.append(semilla / 10000)
    return numeros_generados

def cuadrados_medios_range(semilla, min, max, n):
    numeros = cuadrados_medios(semilla, n).copy()
    numeros_generados.clear()
    for numero in numeros:
        numeros_generados.append((int)(numero * ((max-min)+1) + min))
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

def guardar_en_csv(nombre_archivo='distribucionNormal.csv'):
    # Comprobar si la carpeta CSVs existe, si no, crearla
    carpeta_csv = 'CSVs'
    if not os.path.exists(carpeta_csv):
        os.makedirs(carpeta_csv)

    ruta_archivo = os.path.join(carpeta_csv, nombre_archivo)

    with open(ruta_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['pseudoaleatorios'])
        escritor_csv.writerows(map(lambda x: [x], numeros_generados))

cuadrados_medios_range(7894,20,30,10)
print(numeros_generados)
generar_grafica()