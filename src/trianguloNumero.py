ERROR001 = "ERROR 001: Por favor introduce un número"
def crearFilas(numero:int)->list:
    """Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

    1
    3 1
    5 3 1
    7 5 3 1
    9 7 5 3 1

    Args:
        numero (int): El número con el cual se va a hacer el triángulo de números

    Returns:
        list: devolucion de una lista de listas con todas las iteraciones necesarias para luego imprimirlo por pantalla
    """
    filas = []
    for i in range(1, numero + 1, 2):
        fila = []
        for j in range(i, 0, -2):
            fila.append(j)
        filas.append(fila)
    return filas

if __name__ == "__main__":
    try:
        numero_entero:int = int(input("Ingrese un número entero: "))
        filas_generadas = crearFilas(numero_entero)
        for fila in filas_generadas:
            for numero in fila:
                print(numero, end=" ")
            print()
    except TypeError:
        raise TypeError(ERROR001)