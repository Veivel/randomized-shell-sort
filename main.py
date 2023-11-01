'''
compares Randomized Shellsort and Max-Heap sort
for each dataset. 
'''

import numpy as np
import time
import tracemalloc
import randomizedshellsort as randomizedshellsort
import maxheapsort as maxheapsort
import sys

orig_stdout = sys.stdout
f = open('output.txt', 'w')

# comment this out to print to stdout
sys.stdout = f

print(f"generated at: {time.ctime(time.time())}")

tracemalloc.start()
for key, lst in {
  # 2^9
  "small-sorted": list(range(0, 2**9, 1)),
  "small-reverse": list(range(2**9, 0, -1)),
  "small-random": np.random.randint(0, 2**9, 2**9),
  # 2^13
  "medium-sorted": list(range(0, 2**13, 1)),
  "medium-reverse": list(range(2**13, 0, -1)),
  "medium-random": np.random.randint(0, 2**13, 2**13),
  # 2^16
  "large-sorted": list(range(0, 2**16, 1)),
  "large-reverse": list(range(2**16, 0, -1)),
  "large-random": np.random.randint(0, 2**16, 2**16),
}.items():
  print(f"\n({key})")
  
  lst_kj = sorted(lst)
  np.savetxt(f"dataset/{key}.csv", lst, delimiter =", ", fmt ='% s')
  
  for alg_name, do_sort in {
    "randomizedshellsort": randomizedshellsort.randomized_shell_sort, 
    "maxheapsort": maxheapsort.heapsort
  }.items():
    ts_1 = time.time()
    do_sort(lst) 
    ts_2 = time.time()
    _, peak = tracemalloc.get_traced_memory()
    
    print(f"----- {alg_name} -----")
    print(f"> is correct: {np.array_equiv(lst, lst_kj)}")
    print(f"> memory usage: {peak / 10**6} MB")
    print(f"> time taken: {ts_2 - ts_1:.4f}s")
    
    tracemalloc.reset_peak()

tracemalloc.stop()
sys.stdout = orig_stdout
f.close()