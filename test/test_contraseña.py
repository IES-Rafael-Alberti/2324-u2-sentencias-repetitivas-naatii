from src.contraseña import *
import pytest
@pytest.mark.parametrize(
    "contraseñaUsuario, expected",
    [
        ("pepe", False),
        (1, False),
        ("contraseña", True),
        ("natalia", False),
    ]
)
def test_contraseña(contraseñaUsuario, expected):
    assert adivinarContraseña(contraseñaUsuario) == expected
