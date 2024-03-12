def cuadrados_medios(semilla, n):
    numeros = []
    for _ in range(n):
        semilla = int(str(semilla ** 2).zfill(8)[2:6])
        numeros.append(semilla / 10000)
    return numeros
