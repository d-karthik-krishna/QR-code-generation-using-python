# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time

start_time = time.perf_counter()
def walk_dog():
    time.sleep(8)
    print(("You finishing walking the dog"))
    
def take_trash():
    time.sleep(5)
    print("Trash has been taken out")
    
def get_mail():
    time.sleep(3)
    print("You get a mail")
    
walk_dog()
take_trash()
get_mail()
end_time = time.perf_counter()
print()
print(f"Time taken to finish the tasks without multithreading is {end_time-start_time:.5f}")


#executing all the above three tasks at the same time can be done by:

print()
start_threading = time.perf_counter()

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()#join method helps in printing whats there after after the multithreading after executing the tasks

print()
end_threading = time.perf_counter()
print(f"Time taken to finish the tasks with multithreading is {end_threading-start_threading:.5f}")
