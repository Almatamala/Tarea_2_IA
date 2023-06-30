import matplotlib.pyplot as plt

def scatter_chart(file_name):
    x_values = []
    y_values = []

    # Leer el archivo de texto línea por línea
    with open(file_name, 'r') as file:
        for line in file:
            # Dividir la línea en dos valores separados por una coma
            values = line.strip().split(',')
            x_values.append(float(values[0]))
            y_values.append(float(values[1]))

    # Crear el gráfico de dispersión
    plt.plot(x_values, y_values)
    plt.xlabel('Episodios')
    plt.ylabel('Recompensa acumulada')
    plt.title('Gráfico de dispersión')

    # Mostrar el gráfico
    plt.show()

# Llamar a la función con el nombre del archivo de texto
scatter_chart('Rewards.txt')
