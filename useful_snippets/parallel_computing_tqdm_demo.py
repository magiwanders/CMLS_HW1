import numpy as np
import time
from tqdm import tqdm
from p_tqdm import p_map

# This contains all the inputs to the function that can be parallelized. This example parallelizes 300 instances of an expensive function. As the expensive data takes 0.01 seconds, the WCS is 3 seconds + overhead.
inputs = np.random.rand(3000)
out_trad = []
out_parall = []

def expensive_parallelizable_task(x):
    time.sleep(0.01) # Very expensive! Takes 0.01 seconds
    return x*x

# /////////////////////////////////// TRADITIONAL COMPUTING
t1 = time.time()

for i in tqdm(inputs):
    out_trad.append(expensive_parallelizable_task(i))

t2 = time.time()
print('Traditional computing time: ' + str(t2-t1))

# /////////////////////////////////// PARALLEL COMPUTING
t1 = time.time()

if __name__ == '__main__':
    out_parall = p_map(expensive_parallelizable_task, inputs)

t2 = time.time()
print('Parallel computing time: ' + str(t2-t1))

if out_trad == out_parall:
    print('[SUCCESS] The two computations gave the same result')
else:
    print('[FAIL] Methods are not equivalent')
