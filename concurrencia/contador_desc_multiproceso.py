from multiprocessing import Process
import time

N = 100_000_000

contador_proceso = 0

def contador(n: int) -> None:
    global contador_proceso
    contador_proceso += 1
    print(f"Numero de procesos en paralelo: {contador_proceso}")
    while n > 0:
        n -= 1


if __name__ == '__main__':
    inicio = time.perf_counter()
    p1 = Process(target=contador, args=(N // 2, ))
    p2 = Process(target=contador, args=(N // 2, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")
