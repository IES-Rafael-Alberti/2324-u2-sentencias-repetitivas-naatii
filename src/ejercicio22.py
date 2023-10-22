ERROR001 = "ERROR 001: Por favor introduce un número"
ERROR002 = "ERROR 002: No se puede dividir entre 0"
def esPar(numero:int)->bool:
    """
    Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

    Args:
        numero (int): Número introducido por el usuario.

    Returns:
        bool: _description_
    """
    try:
        return True if numero % 2 != 0 else False
    except ZeroDivisionError:
        raise ZeroDivisionError(ERROR002)    
if __name__=="__main__":
    try:
        numero = 1
        numerosPares = ""
        numerosImpares = ""
        while numero != 0:
            numero = int(input("Introduce un número: "))
            if esPar(numero):
                numerosImpares += str(numero) + " "
            else:
                numerosPares += str(numero) + " "
        else:
            print(f"numeros pares: {numerosPares}\nnumeros Impares: {numerosImpares}")
    except TypeError:
       raise TypeError(ERROR001)