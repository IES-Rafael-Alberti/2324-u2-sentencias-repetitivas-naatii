ERROR001 = "ERROR 001: Por favor introduce un número"
def cuentaAtras(numero:int)->list:
    """Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

    Args:
        cuentaAtras (int): El número del usuario para realizar la cuenta atrás.

    Returns:
        list: la lista de todos número de la cuentra atrás
    """
    numeros = []
    for numero in range(numero, -1, -1): numeros.append(numero)
    return numeros

if __name__ == "__main__":
    try:
        edadInput = int(input("Escribe un número: "))
        print(cuentaAtras(edadInput))
    except TypeError:
        raise TypeError(ERROR001)