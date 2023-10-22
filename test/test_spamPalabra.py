from src.spamPalabra import *
import pytest
@pytest.mark.parametrize(
    "palabra, expected",
    [
        ("natalia", ["natalia", "natalia", "natalia", "natalia", "natalia", "natalia", "natalia", "natalia", "natalia", "natalia"]),
        ("Paco", ["Paco", "Paco", "Paco", "Paco", "Paco", "Paco", "Paco", "Paco", "Paco", "Paco"]),
        ("1", ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"])
    ]
)
def test_spamPalabras(palabra, expected):
    assert spamPalabra(palabra) == expected
