from src.cuentaAtras import *
import pytest
@pytest.mark.parametrize(
    "numero, expected",
    [
        (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
        (5, [5, 4, 3, 2, 1, 0]),
    ]
)
def test_edad(numero, expected):
    assert cuentaAtras(numero) == expected

def test_edadError():
    with pytest.raises(TypeError):
        cuentaAtras("hola")
