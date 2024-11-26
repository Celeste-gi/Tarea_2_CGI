import sys
import matplotlib.pyplot as plt

class Celda:
    def __init__(self, estado=False):
        self.estado = estado

    def interactuar(self, celdas_vecinas):
        celdas_vivas = sum(celda.estado for celda in celdas_vecinas)
        if self.estado:
            return celdas_vivas == 2 or celdas_vivas == 3
        else:
            return celdas_vivas == 3

class Grilla:
    def __init__(self, N, vivas_iniciales, nombre_archivo):
        self.N = N
        self.nombre_archivo = nombre_archivo
        self.celdas = [[Celda() for _ in range(N)] for _ in range(N)]
        for (i, j) in vivas_iniciales:
            self.celdas[i][j].estado = True
        self.contador = 0

    def actualizar_celdas(self, nuevas_celdas):
        for i in range(self.N):
            for j in range(self.N):
                self.celdas[i][j].estado = nuevas_celdas[i][j]

    def visualizar(self):
        matriz = [[1 if self.celdas[i][j].estado else 0 for j in range(self.N)] for i in range(self.N)]
        plt.figure(figsize=(6, 6))
        plt.imshow(matriz, cmap='gray', interpolation='nearest', vmin=0, vmax=1)
        plt.title(f"Paso {self.contador}")
        plt.axis('off')
        plt.savefig(f"{self.nombre_archivo}_{self.contador}.png")
        plt.close()
        print(f"Imagen guardada: {self.nombre_archivo}_{self.contador}.png")

    def avanzar(self):
        nuevas_celdas = [[self.celdas[i][j].interactuar(self.obtener_vecinos(i, j)) for j in range(self.N)] for i in range(self.N)]
        self.actualizar_celdas(nuevas_celdas)
        self.contador += 1
        self.visualizar()

    def obtener_vecinos(self, x, y):
        vecinos = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and 0 <= i < self.N and 0 <= j < self.N:
                    vecinos.append(self.celdas[i][j])
        return vecinos

def leer_datos(archivo_ini):
    with open(archivo_ini, 'r') as file:
        lineas = file.readlines()
    N = int(lineas[0].strip())
    vivas_iniciales = []
    for linea in lineas[1:]:
        if linea.strip():
            x, y = map(int, linea.strip().split(','))
            vivas_iniciales.append((x, y))
    return N, vivas_iniciales

if __name__ == "__main__":
    archivo_ini = sys.argv[1]
    N, vivas_iniciales = leer_datos(archivo_ini)
    grilla = Grilla(N, vivas_iniciales, "conway_output")
    print("Estado inicial:")
    grilla.visualizar()
    pasos = 5
    for i in range(pasos):
        print(f"Generación {i+1}")
        grilla.avanzar()
