
import asyncio
import aiofiles
import matplotlib.pyplot as plt
import time


def generar_archivo(M,N):

    for i in range(M):

        with open(f'original/archivo{i+1}.txt','w') as f:

            f.write('a'* N)

def copia_archivos_sinc(M):

    for i in range (M):
        #aqui leemos el contenido de la carpeta original, lo cual esta contenido por una cantidad M de archivos
        with open(f'original/archivo{i+1}.txt','r') as f1:
            content = f1.read()

        with open(f'copia/archivo{i+1}.txt','w') as copia:
            #aqui estamos copiando los archivos de la carpeta original
            copia.write(content)

async def copia_archivos_asinc(M):

    for i in range(M):
        async with aiofiles.open(f'original/archivo{i+1}.txt','r') as f1:
            content = await f1.read()

        async with aiofiles.open(f'copia/archivo{i+1}.txt','w') as copia:
            await copia.write(content)    

if __name__ == '__main__':

    ##lista_N = [2**i for i in range(10,26)]
    N = 2**20
    lista_M = [2,3,4,5,6,7,8,9,10]
    tiempos_sync = []
    tiempos_async = []

    ## for N in lista_N:
    for M in lista_M:
        #generar_archivo(3,N)  ##parte d)
        generar_archivo(M,N)

        inicio1 = time.perf_counter()
        #copia_archivos_sinc(3)
        copia_archivos_sinc(M)
        fin1 = time.perf_counter()
        tiempo_medido = fin1-inicio1
        tiempos_sync.append(tiempo_medido)

        inicio2 = time.perf_counter()
        #asyncio.run(copia_archivos_asinc(3))
        asyncio.run(copia_archivos_asinc(M))
        fin2 = time.perf_counter()
        tiempo_medido = fin1-inicio1
        tiempos_async.append(tiempo_medido)        
 
#plt.plot(lista_N,tiempos_sync)
#plt.plot(lista_N,tiempos_async)
plt.plot(lista_M,tiempos_sync)
plt.plot(lista_M,tiempos_async)
plt.xlabel('File size [bytes]')
plt.ylabel('Copy time [ms]')
plt.legend(['Sync','Async'])
plt.savefig('SizeVsTime.png')
plt.cla()


