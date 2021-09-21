import cython

from libc.math cimport sqrt


def computar(fim: cython.int, inicio: cython.int = 1):
    """
    Uma função que demora para executar
    """
    pos: cython.int = inicio
    fator: cython.int = 1000 * 1000
    print(pos)
    print(fator)
    
    #Retirando a GIL do Python
    with nogil:
        while pos < fim:
            pos += 1
            sqrt((pos - fator) * (pos - fator))
    print('Acabou')