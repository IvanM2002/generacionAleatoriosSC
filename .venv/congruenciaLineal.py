def congruencia_lineal(semilla, a, c, m, n):
    numeros = []
    for _ in range(n):
        semilla = (a * semilla + c) % m
        numeros.append(semilla / (m - 1))
    return numeros
def congruencia_lineal_range(semilla, a,c,m,n, min, max):
    result = []
    numeros = congruencia_lineal(semilla, a,c,m,n);
    for numero in numeros:
        result.append((int)(numero * ((max-min)+1) + min))
    return result


semilla = 1  # Semilla inicial
a = 9  # pendiente
c = 3  # Intercepto
m = 128  # campo numerico
n = 10  # Cantidad de números aleatorios a generar
numeros_aleatorios = congruencia_lineal(semilla, a, c, m, n)
print(congruencia_lineal_range(semilla, a, c, m, n, min=10,max=15))
