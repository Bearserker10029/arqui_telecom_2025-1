from random import randint
import time


def ejecuta_operacion(datos: list[int], operacion: str) -> float | int | None:

    time.sleep(randint(1, 10))
    match operacion:
        case "promedio":
            resultado = sum(datos) / len(datos)
        case "mediana":
            datos.sort()
            resultado = datos[len(datos) // 2]
        case "maximo":
            datos.sort()
            resultado = datos[-1]
        case "minimo":
            datos.sort()
            resultado = datos[0]
        case _:
            resultado = None

    return resultado


def main():
    datos = [randint(1, 50) for _ in range(500)]
    operaciones = ["promedio", "maximo", "minimo", "mediana"]
    resultados = list()
    for operacion in operaciones:
        resultados.append(ejecuta_operacion(datos, operacion))

    return resultados


if __name__ == '__main__':
    inicio = time.perf_counter()
    res = main()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"El tiempo de ejecucion total es {t_ejecucion:.6f} segundos")
