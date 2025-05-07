from multiprocessing import Pool, cpu_count
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
    num_tareas = 2048

    args = [N // num_tareas] * num_tareas
    inicio = time.perf_counter()
    p = Pool(processes=cpu_count()*2)
    res = p.map(calc_potencia, args)    
    p.close()
    p.join()   
    fin = time.perf_counter()

    print(f"El tiempo total de ejecucion fue: {(fin - inicio):.6f} segundos")
