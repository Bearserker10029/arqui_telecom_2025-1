from itertools import repeat
from multiprocessing import Pool, cpu_count
import time

import numpy as np


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
    num_cpu = cpu_count() * 2

    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    args = zip(mat_M, repeat(vector_A))
    inicio = time.perf_counter()
    
    with Pool(processes=num_cpu) as p:
        resultado = p.starmap(mult_vector, args)

    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecución: {t_ejecucion:.6f} segundos")
