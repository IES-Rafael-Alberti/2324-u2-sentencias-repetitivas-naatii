ERROR001 = "ERROR 001: Por favor introduce un número"

def sumarNumeros(numero:int)->bool:
    """Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

    Args:
        numero (int): Número que introduce el usuario que si es distinto de 0 se va a ir sumando

    Returns:
        bool: verdadero o falso si la suma se puede realizar 
    """
    if type(numero) == int:
        if numero != 0:
            return True
        else:
            return False
    else:
        raise ValueError(ERROR001)

if __name__=="__main__":
    try:
        numero:int = int(input("Introduce un número: "))
        numeroSalida = 0    
        while sumarNumeros(numero):
            numero:int = int(input("Introduce un número: "))
            numeroSalida += numero
        print(numeroSalida)
    except ValueError:
        raise ValueError(ERROR001)