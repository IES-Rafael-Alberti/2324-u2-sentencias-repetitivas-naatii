ERROR001 = "ERROR 001: Por favor introduce un número"
def edad(edad:int)->list:
    """Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

    Args:
        edad (int): La edad del usuario

    Returns:
        list: la lista de todos los años anteriores
    """
    años = []
    for año in range(1, edad+1):
        años.append(año)
    return años

if __name__ == "__main__":
    try:
        edadInput = int(input("Escribe tu edad: "))
        print(edad(edadInput))
    except TypeError:
        raise TypeError(ERROR001)