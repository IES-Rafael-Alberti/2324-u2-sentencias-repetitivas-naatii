ERROR002 = "ERROR 002: Error introduzca un string"
def crearEco(cadena:str)->bool:
    """Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

    Args:
        cadena (str): La cadena a introducir

    Raises:
        AttributeError: Error por si el usuario introduce un número ya que el tipo de dato int no contempla la función lower

    Returns:
        bool: True o None dependiendo de si la cadena es salir o no
    """
    try:
        while cadena.lower() == "salir":
            return True
    except AttributeError:
        raise AttributeError(ERROR002)

if __name__=="__main__":
    cadena:str = input("Introcude una cadena: ")
    while not crearEco(cadena):
        cadena = input("Introcude una cadena: ")
