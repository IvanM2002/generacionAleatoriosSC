def cuadrados_medios(semilla, n):
    numeros = []
    for _ in range(n):
        semilla = int(str(semilla ** 2).zfill(8)[2:6])
        numeros.append(semilla / 10000)
    return numeros


semilla = 3456
n = 10
# numeros_aleatorios = cuadrados_medios(semilla, n)
# print(numeros_aleatorios)

def congruencia_multiplicativo(semilla, a, m, n):
    numeros = []
    for _ in range(n):
        semilla = (a * semilla) % m
        numeros.append(semilla / (m - 1))
    return numeros

semilla = 1  # Semilla inicial
a = 48271       # pendiente
m = 128   # campo numerico
n = 10          # Cantidad de números aleatorios a generar
numeros_aleatorios = congruencia_multiplicativo(semilla, a, m, n)
print(numeros_aleatorios)

