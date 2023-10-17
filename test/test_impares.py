from src.impares import *
import pytest
@pytest.mark.parametrize(
    "imparesUsuario, expected",
    [
        (10, [1, 3, 5, 7, 9]),
    ]
)
def test_edad(imparesUsuario, expected):
    assert impares(imparesUsuario) == expected

def test_edadError():
    with pytest.raises(TypeError):
        impares("hola")
