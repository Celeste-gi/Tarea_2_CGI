import csv

def leer(nombre_archivo):
    primera_columna = []
    otras_columnas = []

    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        encabezados = next(lector_csv)
        num_columnas = len(encabezados)
        
        otras_columnas = [[] for _ in range(num_columnas - 1)]
        
        for fila in lector_csv:
            primera_columna.append(float(fila[0]))  
            for i in range(1, num_columnas):
                otras_columnas[i - 1].append(float(fila[i]))

    return primera_columna, otras_columnas

