import datetime
import math
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor

def main():

    qtd_cores = multiprocessing.cpu_count()

    print(f"Realizando o processamento matemático com {qtd_cores} cores(s).")

    inicio = datetime.datetime.now()
    FINAL = 50_000_000

    #Agora, estamos executando em vários processos
    with Executor(max_workers=qtd_cores) as executor:
        for core_id in range(1, qtd_cores+1):
            ini = FINAL * (core_id - 1)/qtd_cores
            fim = FINAL * core_id / qtd_cores
            print(f'Core {core_id} processando de {ini} até {fim}')
            executor.submit(computar, {'inicio':ini, 'fim': fim})

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

Terminou em 0.33 segundos
"""