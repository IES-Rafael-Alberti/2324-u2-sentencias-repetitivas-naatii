def invertirCadena(cadena:str)->str:
    return cadena[::-1]
if __name__=="__main__":
    cadena = input("introduce una cadena de texto: ")
    for caracter in invertirCadena(cadena): print(caracter, end=" ")
