from random import randint
import socket
from threading import Thread
import time

from notas_utils import calc_nota_final, busca_notas

SOCK_BUFFER = 1024

thread_counter = 0

def handle_client(connection: socket.socket, c_address: tuple[str, int]):
    global thread_counter
    print(f"Conexion de {c_address[0]}:{c_address[1]}")
    thread_counter += 1
    print(f"Total de hilos conectados en este momento: {thread_counter}")

    try:
        while True:
            data = connection.recv(SOCK_BUFFER)
            time.sleep(randint(3, 7))
            if data:
                codigo = data.decode("utf-8")
                valores = busca_notas(codigo)
                nota_final = calc_nota_final(valores)
                connection.sendall(str(nota_final).encode("utf-8"))
            else:
                print("No hay mas datos")
                break
    except IndexError:
        print("No existen notas para el alumno")
    except ConnectionResetError:
        print("El cliente cerro la conexion de manera abrupta")
    finally:
        print("Cerrando la conexion")
        connection.close()
    thread_counter -= 1


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones")
        
        conn, client_address = sock.accept()

        t = Thread(target=handle_client, args=(conn, client_address))
        t.start()


