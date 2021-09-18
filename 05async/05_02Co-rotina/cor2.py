import asyncio

async def diz_oi_demorado():
    print("Oi....")
    #Utilizar 'await' sempre que chamar uma função 
    #assincrona
    await asyncio.sleep(2)
    print('Todos...')

el = asyncio.get_event_loop()
el.run_until_complete(diz_oi_demorado())
el.close()