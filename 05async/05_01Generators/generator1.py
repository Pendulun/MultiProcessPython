from typing import Generator

#Um Generator pode ser visto como uma co-rotina
#Ela será executada, retornará um valor e ficará
#em segundo plano até que seja chamada de novo
#São importantes para o uso de assincronia
def fibo() -> Generator[int, None, None]:
    valor: int = 0
    proximo: int = 1

    while True:
        valor, proximo = proximo, valor + proximo
        yield valor

if __name__ == "__main__":
    for n in fibo():
        print(n, end=', ')
        if n > 100:
            break

    print('\nPronto!')