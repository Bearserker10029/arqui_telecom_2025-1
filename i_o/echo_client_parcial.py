import socket

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("192.168.35.179", 5000)
    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola Mundo! 😊"
    msg_bytes = msg.encode("utf-8")
    print(msg_bytes)

    cantidad_recibida = 0
    cantidad_esperada = len(msg_bytes)

    sock.sendall(msg.encode("utf-8"))

    mensaje = ""
    while cantidad_recibida < cantidad_esperada:
        data = sock.recv(SOCK_BUFFER)
        cantidad_recibida += len(data)
        mensaje += data.decode("utf-8")

    sock.close()

    print(f"Recibi: {mensaje}")
