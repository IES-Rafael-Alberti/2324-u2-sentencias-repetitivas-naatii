from src.sumaDeNumeros import *
import pytest
@pytest.mark.parametrize(
    "numero, expected",
    [
        (0, False),
        (1, True),
        (100, True),
        (-12, True),
        #("asd", True) # ?// Por qué se traga el string?
    ]
)

def test_sumaDeNumeros(numero, expected):
    assert sumarNumeros(numero) == expected

# !// No funciona por que la función se traga el string
def test_sumaDeNumerosError():
    with pytest.raises(ValueError):
        sumarNumeros("asd")
