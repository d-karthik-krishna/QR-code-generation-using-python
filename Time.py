import time

start = time.perf_counter()
print(f"start time is {start}")
print()

for i in range(100000000):
    pass

end = time.perf_counter()
print(f"End time is {end}")
print()
elapse = end - start
print(f"Elapsed time {elapse:.10f}s")


#this is how we calculate the start time 