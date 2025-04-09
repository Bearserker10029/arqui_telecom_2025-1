import time

from notas_utils import calc_nota_final


if __name__ == '__main__':
    inicio = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()

    notas = [int(nota) for nota in contenido.split(",")]    

    nota_final = calc_nota_final(notas)

    fin = time.perf_counter()

    print(f"La nota final es: {nota_final:.1f}")

    t_ejecucion = fin - inicio
    print(f"Tiempo de ejecucion: {t_ejecucion:.6f} segundos")    
