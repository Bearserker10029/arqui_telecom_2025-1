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

