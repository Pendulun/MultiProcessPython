import multiprocessing


def calcular(dado):
    return dado ** 2

def main():
    #Nada impede de criar mais de um processo por core
    tamanho_pool = multiprocessing.cpu_count() * 2

    print(f"Tamanho da pool {tamanho_pool}")
    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f"Saidas: {saidas}")

    #Permite a pool iniciar os processos
    pool.close()
    #O join normal
    pool.join()

if __name__ == "__main__":
    main()