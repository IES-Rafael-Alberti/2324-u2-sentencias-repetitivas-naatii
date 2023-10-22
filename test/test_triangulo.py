from src.triangulo import *
import pytest
@pytest.mark.parametrize(
    "numero, expected",
    [
        (5, ["*", "**", "***", "****", "*****"]),
        (3, ["*", "**", "***"]),
        (2, ["*", "**",])
    ]
)
def test_triangulo(numero, expected):
    assert crearTriangulo(numero) == expected

def test_trianguloError():
    with pytest.raises(TypeError):
        crearTriangulo("hola")
