ERROR001 = "ERROR 001: Por favor introduce un número"
def calculoInversion(inversion:int , interes:int, años:int):
    """Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

    # Formula para calcular El capital tras un año.
    amount *= 1 + interest / 100
    # En donde:
    # - amount: Cantidad a invertir
    # - interest: Interes porcentual anual 

    Args:
        inversion (int): la cantidad a invertir
        interes (int): el porcentaje de interes
        años (int): la cantidad de años

    Returns:
        list: la lista con la cantidad obtenida cada año 
    """
    inveriones = []
    for _ in range(años): 
        inversion *= 1 + interes / 100
        inveriones.append(round(inversion,2))
    return inveriones

if __name__=="__main__":
    try:
        inversion = int(input("Introduce la inversión que va a realizar: "))
        interes = int(input("Introduce el interes: "))
        años = int(input("Introduce el número de años: "))
        for valor in (calculoInversion(inversion, interes, años)): print(valor)
            
    except TypeError:
        raise TypeError(ERROR001)