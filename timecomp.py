import time
from random import randint
from algorithms.sort import quick_sort,selection_sort

def selectionSort(array):
    size=len(array)
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])




list1 = [randint(0,1000) for i in range(20000)]
times=[]
x1=[]
for x in range(0,10001,150):
    start_time = time.time()
    x1.append(x)
    # list2 = selectionSort(list1[:x])
    list2 = selection_sort(list1[:x])
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)
print(times)
import matplotlib.pyplot as plt

plt.xlabel("No. of elements")
plt.ylabel("Time required")
plt.plot(x1,times)
plt.show()
# print(times)
