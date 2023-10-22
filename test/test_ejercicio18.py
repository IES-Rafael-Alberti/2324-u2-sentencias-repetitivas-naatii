from src.ejercicio18 import *
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
def test_sumarComponenteNumeros(numero, expected):
    assert sumarComponenteNumeros(numero) == expected
@pytest.mark.parametrize(
    "numero, expected",
    [
        ("10", "10 "),
        ("20", "20 "),
        ("2", "2 "),
        ("24", "24 "),
        ("123", ""),
        ("55", ""),
    ]
)
def test_esPar(numero, expected):
    assert esPar(numero) == expected
