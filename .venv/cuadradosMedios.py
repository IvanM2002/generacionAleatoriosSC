def cuadrados_medios(semilla, n):
    numeros = []
    for _ in range(n):
        semilla = int(str(semilla ** 2).zfill(8)[2:6])
        numeros.append(semilla / 10000)
    return numeros


semilla = 3456
n = 10
numeros_aleatorios = cuadrados_medios(semilla, n)
print(numeros_aleatorios)
