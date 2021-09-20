import datetime
import math
import asyncio

def main():

    print(f"Realizando o processamento matemático de forma assíncrona.")

    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()
    FINAL = 50_000_000

    #Forma 1
    #el.run_until_complete(computar(inicio=1, fim=FINAL))
    
    #Forma 2
    tarefa1 = el.create_task(computar(inicio=1, fim=10_000_000))
    tarefa2 = el.create_task(computar(inicio=10_000_001, fim=20_000_000))
    tarefa3 = el.create_task(computar(inicio=20_000_001, fim=30_000_000))
    tarefa4 = el.create_task(computar(inicio=30_000_001, fim=40_000_000))
    tarefa5 = el.create_task(computar(inicio=40_000_001, fim=50_000_000))

    tarefas = asyncio.gather(tarefa1, tarefa2,
                    tarefa3, tarefa4, tarefa5)
    el.run_until_complete(tarefas)

    tempo = datetime.datetime.now() - inicio

    print("Terminou em {} segundos".format(tempo.total_seconds()))

async def computar(fim, inicio=1):
    """
    Uma função que demora para executar
    """
    pos = inicio
    fator = 1000 * 1000

    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) ** 2)

if __name__ == "__main__":
    main()

"""
Resultado após uma execução:

Forma 1: Terminou em 34.41 segundos
Forma 2: Terminou em 45.51 segundos
"""