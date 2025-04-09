from random import randint

def genera_notas(nombre_archivo: str = "notas.csv", num_filas: int = 1) -> None:
    """
    Genera un archivo con notas aleatorias en el formato: <codigo>,<notas>
    :param nombre_archivo: string con el nombre y ruta del archivo especifico.
    :param num_filas: entero que indica la cantidad de filas que deben generarse
    :returns: None
    """
    codigo_inicial = 20250001

    contenido = f"codigo,{','.join([f'lab_{idx + 1}' for idx in range(12)])},e1,e2\n"

    for i in range(num_filas):
        fila = f"{codigo_inicial + i},{','.join([str(randint(0,20)) for _ in range(14)])}\n"
        contenido += fila

    with open(nombre_archivo, "w+") as f:
        f.write(contenido)


if __name__ == '__main__':
    genera_notas(num_filas=2)
