
def lee_num(sample_num: int) -> int | None:
    while True:
        try:
            num = input(f"Ingrese un numero para la muestra {sample_num}(presione 'q' para terminar de leer muestras): ")
            if num.lower() == 'q':
                return None
            num =  int(num)
            break
        except ValueError:
            print("Se ingresó un valor incorrecto, inténtelo de nuevo.")
        except KeyboardInterrupt:
            print("\nSe cancelo la operacion, salimos...")
            exit(0)

    return num


if __name__ == '__main__':
    nums = list()

    idx = 1

    while True:
        res_num = lee_num(idx)
        if res_num is None:
            break
        nums.append(res_num)
        idx += 1

    resultado = sum(nums) / len(nums)

    print(f"El resultado del promedio de {idx - 1} numeros es: {resultado}")
