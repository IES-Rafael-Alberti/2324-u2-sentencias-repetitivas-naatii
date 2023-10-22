from src.sumaDeNumeroPositivos import *
import pytest
@pytest.mark.parametrize(
    "numero, expected",
    [
        (0, False),
        (-12, False),
        (1, True),
        (100, True),
    ]
)
def test_sumaDeNumerosPositivos(numero, expected):
    assert sumaDenumeros(numero) == expected

def test_sumaDeNumerosPositivosError():
    with pytest.raises(TypeError):
        sumaDenumeros("asd")
