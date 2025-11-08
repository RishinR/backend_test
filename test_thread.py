import requests
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor

session = requests.Session()

def get_data(url):
    r = session.get(f'http://127.0.0.1:8000/items/{url}')
    print(r.json())

def main():
    urls = range(1, 25000)
    with ThreadPoolExecutor() as executor:
        executor.map(get_data, urls)

if __name__ == '__main__':
    start = perf_counter()
    main()
    end = perf_counter()
    print('time taken: ', end - start)

# time taken: 7.8s