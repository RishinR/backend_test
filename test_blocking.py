import requests
from time import perf_counter

def main():
    urls = range(1, 25000)
    with requests.Session() as session:
        for url in urls:
            r = session.get(f'http://127.0.0.1:8000/items/{url}')
            print(r.json())

if __name__ == '__main__':
    start = perf_counter()
    main()
    end = perf_counter()
    print('time taken: ', end - start)

# time taken 11.1s