import asyncio
import random
import aiofiles

async def sms():
    envio = random.randint(10,100)
    recepcion = random.randint(10,100)
    latencia =  envio + recepcion
    #el tiempo brindado es en mili segundos, por tanto al hacer el asyncio.sleep lo divideremos entre 1000
    await asyncio.sleep(latencia/1000)
    #las latencias no debeen sobreescribir valores antiguos, por eso usamos "a" para que guarde todos los valores
    async with aiofiles.open("latencias_sms.csv", "a") as f:
        await f.write(f"{latencia}\n")
    print(f"La corrutina de la tecnología SMS tuvo una latencia de {latencia} ms")


async def tres_g():
    ida_vuelta = random.randint(100,300)
    procesamiento = random.randint(10,100)
    latencia = 2 * (ida_vuelta + procesamiento)
    await asyncio.sleep(latencia/1000)
    async with aiofiles.open("latencias_3g.csv", "a") as f:
        await f.write(f"{latencia}\n")
    print(f"La corrutina de la tecnología 3G tuvo una latencia de {latencia} ms")


async def satelital():
    retardo = random.randint(500,700)
    procesamiento = random.randint(10,100)
    latencia = 2 * retardo + procesamiento
    await asyncio.sleep(latencia/1000)
    async with aiofiles.open("latencias_satelital.csv", "a") as f:
        await f.write(f"{latencia}\n")
    print(f"La corrutina de la tecnología Satelital tuvo una latencia de {latencia} ms")



async def main():

    await asyncio.gather(sms(), tres_g(), satelital())

if __name__ == "__main__":
    asyncio.run(main())