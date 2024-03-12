import csv

def guardar_numeros_a_csv(numeros, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Numero Aleatorio'])
        for numero in numeros:
            writer.writerow([numero])