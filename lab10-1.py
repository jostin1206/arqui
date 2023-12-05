import csv
import random

#abrimos el archivo csv en modo escritura
with open('pacientes.csv','w', encoding="utf-8") as f:

    #escribimos la fila de encabezados con los nombres de las columnas
    f.write('paciente,edad,diagnostico\n')

    #generamos y escribimos 10 filas de datos para los pacientes
    for i in range(1,11):
        #el numero de pacientes va del 1 al 10
        paciente = i

        #generamos una edad aleatoria entre 20 y 80 años
        edad = random.randint(20,80)

        #generamos un diagnostico aleatorio donde 0 es sano y 1 es enfermo
        diagnostico = random.randint(0,1)

        #escribimos la fila de datos del paciente en el archivo csv
        f.write(f'{paciente},{edad},{diagnostico}\n')



