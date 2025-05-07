import numpy as np
import time

M = 5000
N = 5000

def mult_vector(x: list[np.int32], y: list[np.int32]) -> np.int32:
    """
    Realiza la multiplicación elemento a elemento de dos vectores x y y.
    :param x: lista de números de 32 bits de numpy que representan uno de los vectores a multiplicar
    :param y: lista de números de 32 bits de numpy que representan uno de los vectores a multiplicar
    :returns: entero de 32 bits resultado de la multiplicación
    """
    suma = 0

    for i in range(len(x)):
        suma += x[i] * y[i]
    
    return suma


if __name__ == '__main__':
    resultados = list()

    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    inicio = time.perf_counter()
    for vector in mat_M:
        resultados.append(mult_vector(vector, vector_A))
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecución: {t_ejecucion:.6f} segundos")

