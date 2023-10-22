ERROR001 = "ERROR 001: Por favor introduce un número"

def sumaDenumeros(numero:int)->bool:
    """Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados que sean positivos.

    Args:
        numero (int): Número que introduce el usuario que si es distinto de 0 se va a ir sumando

    Returns:
        bool: verdadero o falso si la suma se puede realizar 
    """
    if numero != 0 and numero > 0:
        return True
    else:
        return False

if __name__=="__main__":
    try:
        numero:int = int(input("Introcude un número: "))
        numeroSalida = 0    
        while sumaDenumeros(numero):
            numero:int = int(input("Introcude un número: "))
            numeroSalida += numero
        print(numeroSalida)
    except TypeError:
        raise TypeError(ERROR001)