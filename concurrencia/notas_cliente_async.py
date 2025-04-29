import asyncio
import time


SOCK_BUFFER = 1024


async def nota_client(codigo: str) -> float:
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 5000)

    #print(f'Send: {codigo!r}')
    writer.write(codigo.encode("utf-8"))
    await writer.drain()

    data = await reader.read(SOCK_BUFFER)
    #print(f'Received: {data.decode("utf-8")!r}')

    #print('Close the connection')
    writer.close()
    await writer.wait_closed()

    return float(data.decode("utf-8"))


async def main(codigos: list[str]) -> list[float]:
    notas = await asyncio.gather(*(nota_client(codigo) for codigo in codigos))

    return notas


if __name__ == '__main__':
    inicio = time.perf_counter()
    notas = asyncio.run(main([f'{20250001 + i}' for i in range(20)]))
    fin = time.perf_counter()

    promedio = sum(notas) / len(notas)

    print(f"Promedio final de notas finales: {promedio}")

    print(f"Tiempo total de ejecucion: {(fin - inicio):.6f} segundos")

