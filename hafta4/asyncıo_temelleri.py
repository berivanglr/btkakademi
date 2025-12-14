import asyncio

async def greet():
    print("Merhaba!")
    await asyncio.sleep(10)
    print("10 saniye sonra: Selam tekrar!")

asyncio.run(greet())
