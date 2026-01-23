''' 
What it is : Running multiple processes at the same time.
Main benefit : True parallel execution on multiple CPU cores.
Why it works : Each process has its own Python interpreter (no GIL).
'''

import multiprocessing
import requests


def downloadFile(url, name):
    print(f"Download {name} Started")
    response = requests.get(url)

    open(f"img_file/file_{name}.jpg", "wb").write(response.content)

    print(f"Download {name} Finished")


url = "https://picsum.photos/2000/3000"

pros = []

if __name__ == "__main__":

    for i in range(1, 6):
        p = multiprocessing.Process(target = downloadFile, args = [url, i])

        p.start()
        pros.append(p)

    for p in pros:
        p.join()
