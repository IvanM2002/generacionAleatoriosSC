def congruencia_multiplicativo(semilla, a, m, n):
    numeros = []
    for _ in range(n):
        semilla = (a * semilla) % m
        numeros.append(semilla / (m - 1))
    return numeros

def congruencia_multiplicativo_range(semilla, a,m,n, min, max):
    result = []
    numeros = congruencia_multiplicativo(semilla, a,m,n);
    for numero in numeros:
        result.append((int)(numero * ((max-min)+1) + min))
    return result


semilla = 1  # Semilla inicial
a = 48271  # pendiente
m = 128  # campo numerico
n = 10  # Cantidad de números aleatorios a generar
print(congruencia_multiplicativo_range(semilla,a,m,n,min=4,max=7))
