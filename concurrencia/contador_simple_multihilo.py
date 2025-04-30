from threading import Thread
import time


def cuenta(ident: int):
    print(f"[Hilo {ident}] Uno")
    time.sleep(1)
    print(f"[Hilo {ident}] Dos")


def main():
    t1 = Thread(target=cuenta, args=(1, ))
    t2 = Thread(target=cuenta, args=(2, ))
    t3 = Thread(target=cuenta, args=(3, ))

    t2.start()
    t1.start()
    t3.start()

    print("[Main] Antes de colocar los Join")

    t1.join()
    t2.join()
    t3.join()

    print("[Main] Despues de colocar los Join")


if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")
    
