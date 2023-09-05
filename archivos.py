def calcular_mediana(datos):
    datos_ordenados = sorted(datos)  # Ordenar los datos de forma ascendente
    n = len(datos_ordenados)  # Obtener la longitud de la lista ordenada

    if n % 2 == 1:  # Si la longitud es impar
        mediana = datos_ordenados[n // 2]  # La mediana es el valor en el medio
    else:  # Si la longitud es par
        mediana = (datos_ordenados[(n - 1) // 2] + datos_ordenados[n // 2]) / 2.0  # Mediana es el promedio de los dos valores medios

    return mediana

# Ejemplo de uso:
conjunto_de_datos = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
mediana = calcular_mediana(conjunto_de_datos)
print(f"La mediana es: {mediana}")


def calcular_media(datos):
    if len(datos) == 0:
        return None  # Manejo de caso especial: la lista está vacía, no se puede calcular la media

    suma = sum(datos)
    media = suma / len(datos)
    return media

# Ejemplo de uso:
conjunto_de_datos = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
media = calcular_media(conjunto_de_datos)

if media is not None:
    print(f"La media es: {media}")
else:
    print("La lista de datos está vacía.")
    

