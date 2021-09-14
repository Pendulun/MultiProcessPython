import datetime
import math
import threading
import multiprocessing

def main():

    qtd_cores = multiprocessing.cpu_count()

    print(f"Realizando o processamento matemático com {qtd_cores} cores(s).")

    inicio = datetime.datetime.now()

    threads = []
    FINAL = 50_000_000

    #Distribuindo o range de execução para cada Thread
    #Apesar de criarmos uma Thread para cada core, ainda não estamos usando paralelismo,
    #Apenas multiThreading
    for core_id in range(1, qtd_cores+1):
        ini = FINAL * (core_id - 1)/qtd_cores
        fim = FINAL * core_id / qtd_cores
        print(f'Core {core_id} processando de {ini} até {fim}')

        #Nesse caso, os dados não são compartilhados, logo, não é necessário lock/unlock
        threads.append(threading.Thread(target=computar, kwargs={'inicio': ini, "fim": fim}, daemon=True))

    [th.start() for th in threads]
    [th.join() for th in threads]

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

Terminou em 19.49 segundos
"""