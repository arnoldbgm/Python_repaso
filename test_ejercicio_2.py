import pytest
from ejercicios_logica import contar_palabras

def test_contar_palabras():
    assert contar_palabras("Hola mundo") == 2
    assert contar_palabras("Esto es una prueba") == 4
    assert contar_palabras("Python es divertido") == 3
