import cuadradosMedios as cm
import csvManager as csvMan

if __name__ == '__main__':
    medios = cm.cuadrados_medios(3456, 10)
    print(medios)
    csvMan.guardar_numeros_a_csv(medios, "cuadardos_medios.csv")