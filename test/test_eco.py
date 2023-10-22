from src.eco import *
import pytest
@pytest.mark.parametrize(
    "cadena, expected",
    [
        ("hola", None),
        ("salir", True),
        ("SALIR", True),
    ]
)
def test_eco(cadena, expected):
    assert crearEco(cadena) == expected

def test_ecoError():
    with pytest.raises(AttributeError):
        crearEco(123)
