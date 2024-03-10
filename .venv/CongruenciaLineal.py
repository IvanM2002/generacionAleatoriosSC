def congruencia_lineal(semilla, a, c, m, n):
    numeros = []
    print(a, m)
    for _ in range(n):
        semilla = (a * semilla + c) % m
        numeros.append(semilla / (m - 1))
    return numeros

semilla = 1  # Semilla inicial
a = 9  # pendiente
c = 3  # Intercepto
m = 128  # campo numerico
n = 10  # Cantidad de números aleatorios a generar
numeros_aleatorios = congruencia_lineal(semilla, a, c, m, n)
print(numeros_aleatorios)