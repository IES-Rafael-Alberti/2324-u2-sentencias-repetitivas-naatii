ERROR001 = "ERROR 001: Por favor introduce un número"

def crearTablas(MINIMO:int, MAXIMO:int)->int:
    """Función que calcula la multiplicación de 2 números

    Args:
        numero (int): El número de la que vamos a sacar la tabla de multiplicar
        multiplicador (int): EL número por el que vamos a multiplicar osea se del 1 al 10

    Returns:
        int: El resultado de la multiplicación
    """
    tablas = []
    for i in range(MINIMO, MAXIMO+1):
        for j in range(MINIMO, MAXIMO+1):
            tablas.append(f"{i} x {j} = {i*j}")
    return tablas

if __name__=="__main__":
    MINIMO = 1
    MAXIMO = 10
    print(crearTablas(MINIMO, MAXIMO))
    for operacion in crearTablas(MINIMO, MAXIMO): print(operacion)