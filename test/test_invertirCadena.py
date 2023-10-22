from src.invertirCadena import *
import pytest
@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("Hola", "aloH"),
        ("123", "321"),
    ]
)
def test_letras(cadena, expected):
    assert invertirCadena(cadena) == expected
