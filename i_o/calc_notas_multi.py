import time

from notas_utils import calc_nota_final


def calc_nota() -> list[float]:
    """
    Realiza el calculo de la nota final y retorna las estadisticas de desempeño.
    :returns: Lista con valores de tiempo de ejecucion total y de cpu.
    """
    inicio = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()

    inicio_cpu = time.perf_counter()
    notas = [int(nota) for nota in contenido.split(",")]    

    nota_final = calc_nota_final(notas)

    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    t_cpu = fin - inicio_cpu

    return [t_ejecucion, t_cpu]


if __name__ == '__main__':
    t_ejecucion_lista = list()
    t_cpu_lista = list()

    for _ in range(10):
        res = calc_nota()
        t_ejecucion_lista.append(res[0])
        t_cpu_lista.append(res[1])

    t_ejecucion_lista.sort()
    t_cpu_lista.sort()

    tep = sum(t_ejecucion_lista) / len(t_ejecucion_lista)
    temed = t_ejecucion_lista[len(t_ejecucion_lista) // 2]
    temax = t_ejecucion_lista[-1]
    temin = t_ejecucion_lista[0]

    print(f"Estadisticas del tiempo de ejecucion -> promedio: {tep:.6f} segundos, mediana: {temed:.6f} segundos, maximo: {temax:.6f} segundos, minimo: {temin:.6f} segundos")

    tcpup = sum(t_cpu_lista) / len(t_cpu_lista)
    tcpumed = t_cpu_lista[len(t_cpu_lista) // 2]
    tcpumax = t_cpu_lista[-1]
    tcpumin = t_cpu_lista[0]

    print(f"Estadisticas del tiempo de cpu -> promedio: {tcpup:.6f} segundos, mediana: {tcpumed:.6f} segundos, maximo: {tcpumax:.6f} segundos, minimo: {tcpumin:.6f} segundos")
