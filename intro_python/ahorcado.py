from random import randint
import time
from typing import Union



def carga_palabras(ruta: str = "palabras.txt", sep: str = "\n") -> list[str]:
    """
    Carga las palabras de la lista de palabras especificada en la ruta. Se puede incluir el separador que se debe utilizar.
    :param ruta: string que contiene la ruta del archivo que vamos a leer.
    :param sep: string que contiene el caracter separador para extraer las palabras.
    :returns: lista de strings que representa todas las palabras que el juego puede tener.
    """
    with open(ruta, "r") as f:
        contenido = f.read()
    
    lista = contenido.split(sep)

    return lista


def actualiza_puntaje(lp: list[str], fallos: int) -> None:
    """
    Imprime el puntaje actual en el terminal con la lista de letras actualizada y el puntaje (cantidad de fallos) actualizada.
    :param lp: Lista que representa las letras de la palabra, con las letras adivinadas siendo mostradas.
    :param fallos: Cantidad de fallos que todavia el usuario puede cometer.
    :returns: None
    """
    print(f"{' '.join(lp)} - Itentos: {fallos}")


def lee_letra() -> str:
    """
    Lee una letra por teclado, valida que el ingreso sea un unico caracter, si no es asi solicita se ingrese de nuevo hasta que la condicion se cumpla.
    :returns: String representando el caracter
    """
    l = ""
    while len(l) != 1:
        l = input("Por favor ingrese una letra: ")
        if len(l) != 1:
            print("Ha ingresado mas de una letra, por favor vuelta a intentarlo")
    
    return l


def busca_letra(p: str, l: str, lp: list[str]) -> Union[list[str], bool]:
    """
    Busca la letra especificada dentro de la palabra para saber si se encuentra dentro de ella. Si se encuentra, 
    se reemplaza en la lista de strings el caracter '_' con la letra correspondiente, en la posicion correspondiente.
    :param p: string que representa a la palabra sobre la cual se hace la busqueda.
    :param l: string que representa a la letra que se va a buscar
    :param lp: lista de strings que representa a la palabra separada con cada caracter de esta siendo un elemento de la lista. Originalmente todos los caracteres estan escondidos ('_')
    :returns: lista de strings que representa a lista de la palabra actualizada y una bandera booleana indicando si la letra se encuentra en la palabra o no.
    """
    letra_encontrada = False

    for idx in range(len(p)):
        if l == p[idx]:
            lp[idx] = l
            letra_encontrada = True

    return lp, letra_encontrada


# palabras = ["arquitectura", "computadoras", "telecomunicaciones", "python", "ahorcado", "universidad", "alumnos", "perro", "proyector"]
palabras = carga_palabras(ruta="palabras.txt", sep="\n")
palabra = palabras[randint(0, len(palabras) - 1)]
lista_palabra = ["_"] * len(palabra)
intentos = 5


if __name__ == '__main__':
    status = ""
    inicio = time.perf_counter()
    while True:
        actualiza_puntaje(lista_palabra, intentos)
        letra = lee_letra()

        lista_palabra, resultado = busca_letra(palabra, letra, lista_palabra)

        if not resultado:
            print("La letra ingresada no se encuentra dentro de la palabra.")
            intentos -= 1

        if intentos == 0:
            print("Lo siento ha perdido el juego 😔")
            status = "perdio"
            break

        if "_" not in lista_palabra:
            print("Felicitaciones! Ha ganado el juego 🎉")
            status = "gano"
            break
    
    fin = time.perf_counter()
    duracion = fin - inicio

    stat = f"{palabra},{status},{duracion},{intentos}\n"

    with open("stats.csv", "a") as f:
        f.write(stat)