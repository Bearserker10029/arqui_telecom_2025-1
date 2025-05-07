from multiprocessing import Process
import time


def calc_potencia(n: int) -> int:
    """
    Calcula la potencia de un número n, donde la expresión es n^n.
    :params n: entero a potenciar, se va a usar tanto como base y exponente.
    :returns: Entero representando la potencia calculada.
    """
    potencia = 1

    cont = n
    while cont > 0:
        potencia *= n
        cont -= 1

    return potencia


if __name__ == '__main__':
    N = 200_000
    proc_num = 512
    inicio = time.perf_counter()
    procesos = list()

    for _ in range(proc_num):
        proceso = Process(target=calc_potencia, args=(N // proc_num, ))
        proceso.start()
        procesos.append(proceso)

    for proceso in procesos:
        proceso.join()
        
    fin = time.perf_counter()

    print(f"El tiempo total de ejecucion fue: {(fin - inicio):.6f} segundos")
