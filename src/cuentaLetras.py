def contarLetras(cadena:str, caracter:str)->int:
    """Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

    Args:
        cadena (str): La cadena de caracteres introducida por usuario
        caracter (str): el caracter introducido por el usuario para poder contarlo

    Returns:
        int: _description_
    """
    contador = 0
    for caracterString in cadena:
        if caracterString==caracter:
            contador += 1 
    return contador

if __name__=="__main__":
    cadena = input("introduce una cadena de texto: ")
    caracter = input("introduce un caracter para contar que esté dentro de la cadena: ")
    
    print(contarLetras(cadena, caracter))