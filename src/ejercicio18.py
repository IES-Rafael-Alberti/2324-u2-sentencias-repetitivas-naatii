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
    return numero
def esPar(numero:int)->str:
    """Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

    Args:
        numero (int): Número introducido por el usuario.

    Returns:
        str: numeros pares de todos los que introduce el usuario.
    """
    numerosPares = ""
    if  int(numero) % 2 == 0:
        numerosPares += numero + " "
    return numerosPares
if __name__=="__main__":
    try:
        numero = "1"
        listaNumerosPares = ""
        while numero != "-1":
            numero:str = input("Ingrese un número: ")
            print(sumarComponenteNumeros(numero))
            listaNumerosPares += esPar(numero)
        print(listaNumerosPares)
    except ValueError:
        raise ValueError(ERROR001)