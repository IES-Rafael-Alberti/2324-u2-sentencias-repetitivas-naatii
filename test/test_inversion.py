from src.inversion import *
import pytest
@pytest.mark.parametrize(
    "inversion, interes, años, expected",
    [
        (100, 12, 3, [112.0, 125.44, 140.49]),
    ]
)
def test_edad(inversion, interes, años, expected):
    assert calculoInversion(inversion, interes, años) == expected

def test_edadError():
    with pytest.raises(TypeError):
        calculoInversion("hola")
