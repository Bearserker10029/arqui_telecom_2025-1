
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
    operaciones = ["promedio", "mediana", "maximo", "minimo"]
    nums = list()

    operacion = input("Por favor indique el tipo de operacion a realizar (promedio/mediana/maximo/minimo): ")

    if operacion.lower() not in operaciones:
        print("Selecciono una opcion invalida, terminando el programa...")
        exit(0)

    idx = 1
    while True:
        res_num = lee_num(idx)
        if res_num is None:
            break
        nums.append(res_num)
        idx += 1
    
    match operacion.lower():
        case "promedio":
            resultado = sum(nums) / len(nums)
        case "mediana":
            nums.sort()
            resultado = nums[len(nums) // 2]
        case "maximo":
            nums.sort()
            resultado = nums[-1]
        case "minimo":
            nums.sort()
            resultado = nums[0]
        case _:
            print("Selecciono una opcion invalida, terminando el programa...")
            exit(0)

    

    print(f"El resultado de la operacion {operacion} de {idx - 1} numeros es: {resultado}")
