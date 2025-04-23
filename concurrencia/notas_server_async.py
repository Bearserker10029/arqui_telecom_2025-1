import asyncio

from notas_utils import calc_nota_final, busca_notas


SOCK_BUFFER = 1024

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("Cliente conectado")

    try:
        while True:
            data = await reader.read(SOCK_BUFFER)
            if data:
                codigo = data.decode("utf-8")
                valores = busca_notas(codigo)
                nota_final = calc_nota_final(valores)

                writer.write(str(nota_final).encode("utf-8"))
                await writer.drain()
            else:
                print("No hay mas datos")
                break
    except IndexError:
        print("No hay notas para este alumno")
    except ConnectionResetError:
        print("El usuario cerró la conexión abruptamente")
    finally:
        writer.close()
        await writer.wait_closed()

    print("conexion cerrada")


async def main():
    server_address = ("0.0.0.0", 5000)

    server = await asyncio.start_server(handle_client, server_address[0], server_address[1])

    async with server:
        print(f"Iniciando el servidor en {server_address[0]}:{server_address[1]}")
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())

