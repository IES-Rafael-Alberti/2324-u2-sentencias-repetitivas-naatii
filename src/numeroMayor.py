ERROR001 = "ERROR 001: Por favor introduce un número"


def obtenerNumeroMaximo(numero:int, numeroSalida:int)->int:
    """Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

    Args:
        numero (int): Número que introduce el usuario que si es distinto de 0 se va a ir sumando

    Returns:
        bool: verdadero o falso si la suma se puede realizar 
    """
    if numero > 0:
        if numero > numeroSalida:
            return numero 
    return numeroSalida
    
if __name__=="__main__":
    try:
        numero = 1
        numeroSalida = 0    
        while numero != 0:
            numero:int = int(input("Introduce un número: "))
            numeroSalida = obtenerNumeroMaximo(numero, numeroSalida)
        print(numeroSalida)
    except ValueError:
        raise ValueError(ERROR001)