def cuadrados_medios(semilla, n):
    numeros = []
    for _ in range(n):
        semilla = int(str(semilla ** 2).zfill(8)[2:6])
        numeros.append(semilla / 10000)
    return numeros

def cuadrados_medios_range(semilla, min, max, n):
    result = []
    numeros = cuadrados_medios(semilla, n);
    for numero in numeros:
        result.append((int)(numero * ((max-min)+1) + min))
    return result

print(cuadrados_medios_range(3456, 4,7, 100))