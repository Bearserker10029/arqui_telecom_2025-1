import asyncio
from random import randint
import time


async def cuenta(ident: int):
    print(f"[{ident}] Uno")
    await asyncio.sleep(randint(1, 5))
    print(f"[{ident}]Dos")


async def main():
    await asyncio.gather(*(cuenta(idx) for idx in range(3)))


if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")
