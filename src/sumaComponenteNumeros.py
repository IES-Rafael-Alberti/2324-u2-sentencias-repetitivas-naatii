ERROR001 = "ERROR 001: Por favor introduce un número"

def sumarComponenteNumeros(numero:int)->int:
    """Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

    Args:
        numero (int): numero ingresado por consola

    Returns:
        int: La suma del número
    """
    if int(numero) > 0:
        suma = 0
        for digito in numero:
            suma += int(digito)
        return suma

if __name__=="__main__":
    try:
        numero:int = input("Ingrese un número: ")
        print(sumarComponenteNumeros(numero))
    except ValueError:
        raise ValueError(ERROR001)