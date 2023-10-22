from src.primoONo import *
import pytest
@pytest.mark.parametrize(
    "numero, expected",
    [
        (10, False),
        (9, True),
        (11, True),
        (7, True),
    ]
)
def test_esPrimo(numero, expected):
    assert es_primo(numero) == expected

def test_esPrimoError():
    with pytest.raises(TypeError):
        es_primo("hola")
