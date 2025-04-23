
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


def calc_nota_final(notas: list[int]) -> float:
    """
    Calcula la nota final del curso Arquitectura de Computadoras, usando la formula del silabo.
    :param notas: lista de enteros que representan las notas a calcular.
    :returns: resultado del calculo de la nota final.
    """
    notas_labs = notas[:12]
    e1 = notas[12]
    e2 = notas[13]
    
    nota_lab = sum(notas_labs) / len(notas_labs)

    nota_final = ((5 * nota_lab) + (2.5 * e1) + (2.5 * e2)) / 10

    return nota_final


if __name__ == '__main__':
    print("hola mundo")

