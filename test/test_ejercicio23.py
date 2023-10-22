from src.ejercicio23 import *
import pytest
@pytest.mark.parametrize(
    "titulo, expected",
    [
        ("Los 3 mosqueteros", 1),
        ("Historia de 2 ciudades", 1),
        ("20000 leguas de viaje submarino", 5),
    ]
)
def test_contarNumeros(titulo, expected):
    assert calculaNumeros(titulo) == expected
  