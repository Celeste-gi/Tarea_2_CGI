import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

def plot1D(x, y, xlabel, ylabel, output_file):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(output_file)
    plt.close()

def plot2D(x, y, values, xlabel, ylabel, output_file):
    plt.figure()
    plt.scatter(x, y, c=values, cmap='viridis')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar(label="Values")
    plt.savefig(output_file)
    plt.close()

