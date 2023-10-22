from src.edad import *
import pytest
@pytest.mark.parametrize(
    "edadUsuario, expected",
    [
        (10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ]
)
def test_edad(edadUsuario, expected):
    assert edad(edadUsuario) == expected

def test_edadError():
    with pytest.raises(TypeError):
        edad("hola")
