def comprobarCaracter(cadena:str, caracter:str)->str:
    """
    Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

    Args:
        cadena (str): La cadena de texto ingresada por usuario.

    Returns:
        str: posición si encuentra el caracter en la cadena
    """
    contador = ""
    for index, caracterCadena in enumerate(cadena.lower()):
        if caracter == caracterCadena:
            contador += str(index) + " "
        else:
            contador += ""
    return contador
if __name__ == "__main__":
    cadena:str = input("introduce una cadena de texto: ")
    caracter:str = input("introduce un caracter: ")
    print(comprobarCaracter(cadena, caracter))