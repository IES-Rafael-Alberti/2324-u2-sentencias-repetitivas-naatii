from src.trianguloNumero import *
import pytest
@pytest.mark.parametrize(
    "numero, expected",
    [
        (5, [[1], [3, 1], [5, 3, 1]]),
        (3, [[1], [3, 1]]),
        (2, [[1]])
    ]
)
def test_triangulo(numero, expected):
    assert crearFilas(numero) == expected

def test_trianguloError():
    with pytest.raises(TypeError):
        crearFilas("hola")
