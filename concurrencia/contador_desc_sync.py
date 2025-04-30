import time


N = 100_000_000

def contador(n: int):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    contador(N)
    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")
