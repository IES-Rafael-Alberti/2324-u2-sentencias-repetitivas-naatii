from src.numeroMayor import *
import pytest
@pytest.mark.parametrize(
    "numero, numeroSalida, expected",
    [
        (10, 5, 10),
        (10, 10, 10),
        (5, 10, 10),
        (2, 3, 3),

    ]
)
def test_numeroMayor(numero,numeroSalida, expected):
    assert obtenerNumeroMaximo(numero, numeroSalida) == expected

def test_edadError():
    with pytest.raises(TypeError):
        obtenerNumeroMaximo("hola")
