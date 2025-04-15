import socket

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("192.168.35.179", 5000)
    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola Mundo!"

    sock.sendall(msg.encode("utf-8"))
    data = sock.recv(SOCK_BUFFER)

    sock.close()

    print(f"Recibi: {data}")
