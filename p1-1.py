import sys
from read import leer

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 p1-1.py 'archivo.csv'")
        sys.exit(1)
        
    nombre_archivo = sys.argv[1]
    primera_columna, otras_columnas = leer(nombre_archivo)
    
    print("Columna 1 (primeros 5 elementos):", primera_columna[:5] if len(primera_columna) >= 5 else primera_columna)
    
    for i, columna in enumerate(otras_columnas, start=1):
        print(f"Columna {i+1} (primeros 5 elementos):", columna[:5] if len(columna) >= 5 else columna)

