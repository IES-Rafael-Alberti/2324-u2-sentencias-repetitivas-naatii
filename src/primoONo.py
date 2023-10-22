ERROR001 = "ERROR 001: Por favor introduce un número"
def es_primo(numero:int)->bool:
    """Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

    Args:
        numero (int): Número introducido por el usuario.

    Returns:
        bool: _description_
    """
    if numero<2:
        return False
    for i in range(2, numero):
        if  (numero % i)== 0:
            return False
        else:
            return True

if __name__=="__main__":
    try:
        numero = int(input("Introduce un número: "))
        print("Es primo") if es_primo(numero) else print("No es primo")
    except TypeError:
       raise TypeError(ERROR001)