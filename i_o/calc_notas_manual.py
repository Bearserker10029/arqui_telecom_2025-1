import time

if __name__ == '__main__':
    inicio = time.perf_counter()
    nombres = f"{','.join([f'Lab {idx + 1}' for idx in range(12)])},examen 1,examen 2".split(",")

    notas = list()

    for nombre in nombres:
        nota = input(f"Ingrese la nota de {nombre}: ")
        nota = int(nota)
        notas.append(nota)

    inicio_cpu = time.perf_counter()
    notas_labs = notas[:12]
    e1 = notas[12]
    e2 = notas[13]
    
    nota_lab = sum(notas_labs) / len(notas_labs)

    nota_final = ((5 * nota_lab) + (2.5 * e1) + (2.5 * e2)) / 10

    fin = time.perf_counter()
    print(f"La nota final es: {nota_final}")

    t_ejecucion = fin - inicio
    t_cpu = fin - inicio_cpu
    ratio_io = ((t_ejecucion - t_cpu) / t_ejecucion) * 100

    print(f"Tiempo de ejecucion total: {t_ejecucion:.5f} segundos - Tiempo de cpu: {t_cpu:.5f} segundos - Fraccion de operaciones I/O: {ratio_io:.2f}%")
