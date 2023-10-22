def calculaNumeros(titulo:str)->str:
    """
    Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

    Ejemplo de ejecución:
    Libro: Los 3 mosqueteros
    Libro: Historia de 2 ciudades
    Libro: /
    Línea completa. Aparecen 2 dígitos numéricos.
    Libro: 20000 leguas de viaje submarino
    Libro: El señor de los anillos
    Libro: /
    Línea completa. Aparecen 5 dígitos numéricos.
    Libro: 20 años después
    Libro: *
    Fin. Se leyeron 2 líneas completas.

    Args:
        titulo (str): _description_

    Returns:
        str: _description_
    """
    numeros = 0
    for numero in titulo:
        if numero.isdigit():
            numeros += 1
    return numeros

if __name__=="__main__":
    titulo = ""
    numeros = 0
    numeroDeLineas = 0
    while titulo != "*":
        titulo = input("Ingrese titulo del libro: ")
        numeros += calculaNumeros(titulo)
        if titulo == "/":
            print(f"Línea completa. Aparecen {numeros} dígitos numéricos.")
            numeroDeLineas += 1
    print(f"Fin. Se leyeron {numeroDeLineas} líneas completas.")