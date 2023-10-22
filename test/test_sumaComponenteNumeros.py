from src.sumaComponenteNumeros import *
import pytest
@pytest.mark.parametrize(
    "numero, expected",
    [
        ("10", 1),
        ("20", 2),
        ("2", 2),
        ("24", 6),
        ("123", 6),
        ("55", 10),
    ]
)
def test_sumaComponentesNumeros(numero, expected):
    assert sumarComponenteNumeros(numero) == expected

