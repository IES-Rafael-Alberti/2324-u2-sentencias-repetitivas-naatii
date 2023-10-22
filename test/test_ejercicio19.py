from src.ejercicio19 import *
import pytest
help = (
"""
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
""")
@pytest.mark.parametrize(
    "opcion, expected",
    [
        ("1", "[>] Comenzando programa..."),
        ("2", "[>] Imprimiendo listado..."),
        ("3", "[>] Saliendo del programa"),
        ("4", help),
    ]
)
def test_menu(opcion, expected):
    assert menu(opcion) == expected
