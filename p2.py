import time
import concurrent.futures
import requests
import statistics
urls = [
"https://www.wikipedia.org/",
"https://www.nytimes.com/",
"https://www.bbc.com/",
"https://www.python.org/",
"https://www.reddit.com/",
"https://www.instagram.com/",
"https://www.twitter.com/",
"https://www.cnn.com/",
"https://www.github.com/",
"https://www.spotify.com/",
]

def parte_a():
    inicio = time.perf_counter()
    i = 1
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:

            with open(f'pagina{i}.html', 'w', encoding = "utf-8") as f:
                f.write(response.text)

            i += 1 
    
    fin = time.perf_counter()
    time_a = fin - inicio
    return time_a
    ##print(f"Tiempo de ejecucion(a) : {fin-inicio}")

def parte_b():
    inicio = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        for url in urls:
            executor.submit(parte_a,url)
    fin = time.perf_counter()
    time_b =  fin -inicio
    return time_b
    ##print(f"Tiempo de ejecucion(b) : {fin-inicio}")

def tiempo_a():
    tiempos_a = []
    for _ in range (5):

        times = parte_a()
        tiempos_a.append(times)

        return statistics.median(tiempos_a)

def tiempo_b():
    tiempos_b = []
    for _ in range(5):
        times = parte_b()
        tiempos_b.append(times)

        return statistics.median(tiempos_b)

if __name__ == "__main__":

    parte_a()
    t1 = tiempo_a()
    parte_b()
    t2 = tiempo_b()

    print(f"Tiempo parte a: {t1}")
    print(f"Tiempo parte b: {t2}")




