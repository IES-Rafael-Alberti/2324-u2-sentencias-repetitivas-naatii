ERROR001 = "ERROR 001: Por favor introduce un número"
def crearTriangulo(numero:int)->list:
    """Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

    Args:
        numero (int): La altura que va a tener el triángulo.

    Returns:
        list: La lista con cada nivel del triágulo para imprimirlo posteriormente por pantalla. 
    """
    triangulo = []
    simbolo = '*'
    for i in range(numero):
        triangulo.append(simbolo*(i+1))
    return triangulo

if __name__=="__main__":
    try:
        numero:int = int(input("Introduce un número: "))
        for fila in crearTriangulo(numero): print(fila)
    except TypeError:
        raise TypeError(ERROR001)