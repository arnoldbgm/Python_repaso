import pytest
from ejercicios_logica import sumar_numeros

def test_sumar_numeros():
    assert sumar_numeros(5) == 15  # 1 + 2 + 3 + 4 + 5 = 15
    assert sumar_numeros(10) == 55  # 1 + 2 + ... + 10 = 55
