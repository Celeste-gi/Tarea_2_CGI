import sys
import pandas as pd
import matplotlib.pyplot as plt

csv_file = sys.argv[1]
output_image = sys.argv[2]


data = pd.read_csv(csv_file)


plt.plot(data["tiempo"], data["v1"], label="v1", marker="o")
plt.xlabel("Tiempo")
plt.ylabel("v1")
plt.legend()
plt.title("Gráfico de Tiempo vs v1")


plt.savefig(output_image)
print(f"Gráfico guardado en {output_image}")
