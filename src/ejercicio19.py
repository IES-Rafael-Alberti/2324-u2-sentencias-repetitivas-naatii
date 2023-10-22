help = """
                   __  .__.__  .__          
  ____ _____ _/  |_|__|  | |  | _____   
 /    \\__  \\   __\  |  | |  | \__  \  
|   |  \/ __ \|  | |  |  |_|  |__/ __ \_
|___|  (____  /__| |__|____/____(____  /
     \/     \/                       \/ 
Ayuda del menú:
    [>] opción 1 -> Comenzar programa
    [>] opción 2 -> Imprimir listato
    [>] opción 3 -> Salir del programa
"""
OPCION1 = "[>] Comenzando programa..."
OPCION2 = "[>] Imprimiendo listado..."
OPCION3 = "[>] Saliendo del programa"

# ? Para que quiero esto?
# ? Como hacer que esta función tenga sentido?
# ?// devolviento el número?
# ? Devolviento true o false?
# * Devolver un string
# todo: revistar esto
def menu(opcion: str) -> str:
    """
    Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.

    Args:
        opcion (str): La opción seleccionada por el usuario

    Returns:
        str: La devolución de lo que se va a mostrar por pantalla
    """
    match opcion:
        case "1":
            return( OPCION1)
        case "2":
            return( OPCION2)
        case "3":
            return OPCION3
        case other:
            return( help)

if __name__ == "__main__":
    option = ""
    while option != OPCION3:
        option = menu(input("introduce un número del 1 - 3: "))
        print(option)
