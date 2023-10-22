from src.ejercicio20 import *
import pytest

@pytest.mark.parametrize(
    "cadena, caracter, expected",
    [
        ("Hola que tal estas", "a", "3 10 16 "),
        ("Natalia tiene noticiones", "n", "0 11 14 21 "),
    ]   
)
def test_comprobarCaracter(cadena, caracter, expected):
    assert comprobarCaracter(cadena, caracter) == expected