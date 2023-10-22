from src.ejercicio21 import *
import pytest
@pytest.mark.parametrize(
    "monto, expected",
    [
        (1001, 100.1),
        (100, 100),
        (1, 1),
        (-12, procesarMonto(-12))
    ]
)
def test_monto(monto, expected):
    assert procesarMonto(monto) == expected
