import socket
import time

from notas_utils import calc_nota_final


SOCK_BUFFER = 1024

with open("notas.csv", "r") as f:
    contenido = f.read()

filas = contenido.split("\n")


def busca_notas(codigo: str) -> list[int]:
    """
    Busca las notas correspondientes al codigo proporcionado en la base de datos de notas (archivo CSV)
    :param codigo: string que representa al codigo a buscar
    :returns: lista de enteros con las notas a encontrar
    """
    res = ""
    for fila in filas:
        if codigo in fila:
            res = fila
            break

    if res == "":
        return list()
    
    notas = [int(val) for val in res.split(",")][1:]

    return notas


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        
        conn, client = sock.accept()

        print(f"Conexion de {client[0]}:{client[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)

                if data:
                    #print(f"Recibi: {data}")
                    inicio = time.perf_counter()
                    codigo = data.decode("utf-8")
                    valores = busca_notas(codigo)
                    nota_final = calc_nota_final(valores)
                    fin_cpu = time.perf_counter()
                    conn.sendall(str(nota_final).encode("utf-8"))
                    fin = time.perf_counter()
                else:
                    print(f"No hay mas datos")
                    break
        except ConnectionResetError:
            print("El cliente cerro la conexion de manera abrupta")
        except KeyboardInterrupt:
            print("El usuario termino el programa")
        finally:
            print("Cerrando la conexion")
            conn.close()
            print(f"Total de operacion: {(fin - inicio):.6f} segundos")
            print(f"Total de CPU: {(fin_cpu - inicio):.6f} segundos")
            print(f"Total de transmision: {(fin - fin_cpu):.6f} segundos")
