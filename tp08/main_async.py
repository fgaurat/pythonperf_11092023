import asyncio


async def add(a,b):
    await asyncio.sleep(0.5)
    return a+b



def toto():
    pass
async def main():
    # print('Hello ...')
    # asyncio.sleep(1)
    # print('... World!')

    # r = await add(1,2)

    # print(r)

    all_r = [add(1,2),add(18,25),add(81,42),add(1,28)]
    
    r = await asyncio.gather(*all_r)
    print(r)
if __name__=='__main__':
    asyncio.run(main())
