# Constantes
NUMERO:int = 10
ERROR001:TypeError = "ERROR 001: Por favor introduzca un número"

# Core
# TODO: Preguntar si esto está bien
# ?//: Devolver solo la palabra sirve para algo?
# ?//: No sería mejor hacer el bucle dentro de la función?
# ?*: Usando listas?
# ?//: print dentro de la función?
# ?//: llama recursiva a otra función?
def spamPalabra(palabra:str)->str:
    palabras:list = []
    """Función que devuelve una palabra.
    Args:
        palabra (str): La palabra recibida para poder devolverla

    Returns:
        str: la devolución de la lista con todas las palabras
    """
    for _ in range(NUMERO):
        palabras.append(palabra) 
    return palabras

if __name__ == "__main__":
    # ! Esto no saldrá en el test 
    # TODO: Pensar en un posible refactor de esto
    palabra:str = input("Introduce una palabra: ")
    listaPalabras = spamPalabra(palabra)
    for palabra in listaPalabras:
        print(palabra)
