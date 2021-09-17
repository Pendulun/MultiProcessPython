import multiprocessing

print(f'Imprimindo contexto global do processo com nome: {multiprocessing.current_process().name}')
def faz_algo(valor):
    print(f'Fazendo algo com o {valor} no processo {multiprocessing.current_process().name}')

def main():
    print(f'Iniciando o processo com nome: {multiprocessing.current_process().name}')
    pc = multiprocessing.Process(target=faz_algo, args=('Pássaro',), name='Processo Geek')

    print(f'Iniciando o processo com nome: {pc.name}')

    pc.start()
    pc.join()

if __name__ == '__main__':
    print(f'Chamando main do processo: {multiprocessing.current_process().name}')
    main()