import datetime
import math

def main():
    inicio = datetime.datetime.now()

    computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio

    print("Terminou em {} segundos".format(tempo.total_seconds()))

def computar(fim, inicio=1):
    """
    Uma função que demora para executar
    """
    pos = inicio
    fator = 1000 * 1000

    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == "__main__":
    main()

"""
Resultado após uma execução:

Terminou em 21.692998 segundos
"""