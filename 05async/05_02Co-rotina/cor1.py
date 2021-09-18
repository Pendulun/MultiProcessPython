import asyncio

async def diz_oi():
    print('Oi...')

ev_loop = asyncio.get_event_loop()

ev_loop.run_until_complete(diz_oi())
ev_loop.close()