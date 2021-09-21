import datetime
import computa

def main():
    inicio = datetime.datetime.now()

    computa.computar(fim=50_000_000)

    tempo = datetime.datetime.now() - inicio

    print("Terminou em {} segundos".format(tempo.total_seconds()))

if __name__ == "__main__":
    main()

"""
Resultado após uma execução:

Apenas compilando em Cython:
Terminou em 20.42 segundos

Alterando 'computa' para usar cython:
Terminou em 0.001 segundos

Alterando 'computa' para ignorar a GIL:
Terminou em 0.0 segundos
"""