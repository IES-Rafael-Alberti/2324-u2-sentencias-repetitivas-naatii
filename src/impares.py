ERROR001 = "ERROR 001: Por favor introduce un número"
def impares(numero:int)->list:
    """Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

    Args:
        numero (int): el número que le vamos a pasar para que calcule todos los impares hasta ese número.

    Returns:
        list: devuelve la lista con todos los impares en el rango de números que el usuario ha introducido por parametro.
    """
    impares:list = []
    for impar in range(numero): 
        impares.append(impar) if impar % 2 != 0 else None
    return impares

if __name__=="__main__":
    try:
        numero:int = int(input("Introduce un número: "))
        print(impares(numero))
    except TypeError:
        raise TypeError(ERROR001)
