import asyncio
import aiofiles

async def exemplo_arq1():
    async with aiofiles.open('texto.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)

async def exemplo_arq2():
    async with aiofiles.open('links.txt') as arquivo:
        async for linha in arquivo:
            print(linha)

def main():
    el = asyncio.get_event_loop()

    el.run_until_complete(exemplo_arq1())
    el.run_until_complete(exemplo_arq2())

    el.close()

    """
    tar1 = el.create_task(exemplo_arq1())
    tar2 = el.create_task(exemplo_arq2())

    tarefas = asyncio.gather(tar1, tar2)

    el.run_until_complete(tarefas)
    """


if __name__ == '__main__':
    main()
