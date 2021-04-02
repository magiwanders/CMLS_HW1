from multiprocessing import Pool
import numpy as np
import time

# This contains all the inputs to the function that can be parallelized. This example parallelizes 300 instances of an expensive function. As the expensive data takes 0.01 seconds, the WCS is 3 seconds + overhead.
inputs = np.random.rand(300)

def expensive_parallelizable_task(x):
    time.sleep(0.01) # Very expensive! Takes 0.01 seconds

# /////////////////////////////////// TRADITIONAL COMPUTING
t1 = time.time()

for i in inputs:
    expensive_parallelizable_task(i)

t2 = time.time()
print('Traditional computing time: ' + str(t2-t1))

# /////////////////////////////////// PARALLEL COMPUTING
t1 = time.time()

with Pool() as p: # Pool(n) forces n threads
        p.map(expensive_parallelizable_task, inputs)

t2 = time.time()
print('Parallel computing time: ' + str(t2-t1))
