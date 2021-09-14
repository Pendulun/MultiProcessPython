import multiprocessing


def calcular(dado):
    return dado ** 2

def imprimir_nome_processo():
    print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')

def main():
    #Nada impede de criar mais de um processo por core
    tamanho_pool = multiprocessing.cpu_count() * 2

    print(f"Tamanho da pool {tamanho_pool}")

    #Initializer indica uma função que será chamada assim que
    #um novo processo for criado
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f"Saidas: {saidas}")

    #Permite a pool iniciar os processos
    pool.close()
    #O join normal
    pool.join()

if __name__ == "__main__":
    main()