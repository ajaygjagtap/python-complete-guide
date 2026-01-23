''' 
What it is : Running multiple threads inside one program.
Main use : Spped up I/O-bound tasks (network calls, file reads, waiting).
Limitation : Because of the GIL, threads do not run CPU-heavy code in parallel.
Threads run concurrently (but not in parallel for CPU work).
'''

import threading
from concurrent.futures import ThreadPoolExecutor
import time 

def task(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


time1 = time.perf_counter()
# Normal Code
# task(4)
# task(2)
# task(1)



# Same code using Threads
t1 = threading.Thread(target = task, args = [4])
t2 = threading.Thread(target = task, args = [2])
t3 = threading.Thread(target = task, args = [1])

# .start() begins the Thread
t1.start()
t2.start()
t3.start()

# .join() waits for the Thread to finish
t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
print(time2 - time1)

print("-----------------------------------------------------------------------------")

def work():
    with ThreadPoolExecutor( ) as executor:
        f1 = executor.submit(task, 3)
        f2 = executor.submit(task, 2)
        f3 = executor.submit(task, 4)

        print(f1.result())
        print(f2.result())
        print(f3.result())


        l = [3, 5, 1, 2]
        results1 = executor.map(task, l)

        for r in results1:
            print(r)

work()