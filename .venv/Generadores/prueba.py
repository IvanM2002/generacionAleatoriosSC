import random

class GeneradorUniforme:
    def __init__(self):
        # Parámetros del generador con distribucion Uniforme 
        self.maxI = 10                      #Intervalo superior
        self.minI = 0                       #Intervalo Inferior
        self.ni = []                        #Numeros Ni
        self.nuIntervalos = 8               #Numero de intervalos para la grafica
        # Parámetros del generador lineal congruencial
        self.a = 1664525                    #Pendiente  = {a E Z | 1 <= a < m}
        self.c = 1013904223                 #Intersección = {c E Z | 0 <= C < m} 
        self.m = 2**32                      #Conjunto = {m E Z | m > 0} 
        self.semilla = None                 #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m}
        self.ri = []                        #Numeros Ri


    # Función para generar Ri con congruencia Lineal
    def generar_ri(self, total):
        if self.semilla is None:
            self.semilla = random.randint(0, self.m - 1) #Semilla -> [0,m)  = {Xo E Z | 0 <= Xo < m} se utiliza unicamente para generar una semilla si no se especifica una

        for _ in range(total):
            self.semilla = (self.a * self.semilla + self.c) % self.m
            self.ri.append(self.semilla / (self.m - 1))

    # Función para generar Ni con distribucion Uniforme
    def generar_distr_uniforme(self, total):
        self.generar_ri(total)
        self.ni = [(self.minI + (self.maxI - self.minI) * N) for N in self.ri]
        return self.ni

    def generar(self):
        self.ni = self.generar_distr_uniforme(10000)
