import time

from generador_notas import genera_notas
from notas_utils import calc_nota_final


def calc_nota(num_filas: int = 1) -> list[float]:
    """
    Realiza el calculo de la nota final y retorna las estadisticas de desempeño.
    :param num_filas: Entero que indica cuantas filas deben ser generaas.
    :returns: Lista con valores de tiempo de ejecucion total y de cpu.
    """
    genera_notas(num_filas=num_filas)
    
    inicio = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()

    inicio_cpu = time.perf_counter()
    contenido = contenido.split("\n")[1:]
    for fila in contenido:
        if len(fila) < 1:
            continue
        valores = [int(valor) for valor in fila.split(",")]    
        notas = valores[1:]
        nota_final = calc_nota_final(notas)

    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    t_cpu = fin - inicio_cpu

    return [t_ejecucion, t_cpu]


if __name__ == '__main__':
    te_1f = list()
    t_cpu_1f = list()

    te_10f = list()
    t_cpu_10f = list()

    te_100f = list()
    t_cpu_100f = list()

    for _ in range(10):
        res = calc_nota(num_filas=1)
        te_1f.append(res[0])
        t_cpu_1f.append(res[1])

    te_1f.sort()
    t_cpu_1f.sort()

    for _ in range(10):
        res = calc_nota(num_filas=10)
        te_10f.append(res[0])
        t_cpu_10f.append(res[1])

    te_10f.sort()
    t_cpu_10f.sort()

    for _ in range(10):
        res = calc_nota(num_filas=100)
        te_100f.append(res[0])
        t_cpu_100f.append(res[1])

    te_100f.sort()
    t_cpu_100f.sort()

    te1fm = te_1f[len(te_1f) // 2]
    te10fm = te_10f[len(te_10f) // 2]
    te100fm = te_100f[len(te_100f) // 2]

    tcpu1fm = t_cpu_1f[len(t_cpu_1f) // 2]
    tcpu10fm = t_cpu_10f[len(t_cpu_10f) // 2]
    tcpu100fm = t_cpu_100f[len(t_cpu_100f) // 2]

    print(f"Valores de mediana para tiempos de ejecucion -> 1 fila: {te1fm:.6f} segundos, 10 filas: {te10fm:.6f} segundos, 100 fila: {te100fm:.6f} segundos")
    print(f"Valores de mediana para tiempos de CPU -> 1 fila: {tcpu1fm:.6f} segundos, 10 filas: {tcpu10fm:.6f} segundos, 100 fila: {tcpu100fm:.6f} segundos")