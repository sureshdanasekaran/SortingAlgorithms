# Sorting algorithms insertion sort, selection sort and quicksort using median of three
import time
import numpy as np
import sys

sys.setrecursionlimit(2**31-1)

argumentList = sys.argv 

arg1 = sys.argv[1]
arg2 = int(sys.argv[-2])
arg3 = sys.argv[-1]

#print(arg1, arg2, arg3)
tempArray = []

def insertionSort(data, arrlength):
   for i in range(1,arrlength):
       current_element = data[i]
       #the current element and sorted elements are compared and swapped
       while i>0 and (data[i-1] > current_element):    
           data[i] = data[i-1]
           i = i-1
       data[i] = current_element


def selectionSort(data, arraylength):
  for i in range(arraylength):
    # let the unsorted part be min_index.
    min_index = i
    for j in range(i+1, arraylength):
      if (data[j] < data[min_index]):
        min_index = j # updating the min_index based on smaller element
    # Swap the element with unsorted     
    temp = data[i]
    data[i] = data[min_index]
    data[min_index] = temp
    
  return data
   

#function to find the median of three numbers
def median(first, center, last):
   # x = min(first,center,last)
   # y = max(a,b,c)
    median_value = (first+center+last)-(min(first,center,last) + max(first,center,last))
    return median_value

# partitioning function around the median
def medianofthree_partitioning(array, leftpointer, rightpointer):
    left = array[leftpointer]
    right = array[rightpointer-1]
    length = rightpointer - leftpointer + 1
    if length % 2 == 0:
        middle_element = array[leftpointer + length//2 - 1]
    else:
        middle_element = array[leftpointer + length//2]

    pivot = median(left, right, middle_element)
    pivotindex = array.index(pivot) 
    #swap with the left to act as pivot
    array[pivotindex] = array[leftpointer]
    array[leftpointer] = pivot

    i = leftpointer + 1
    for j in range(leftpointer + 1, rightpointer):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    leftdata = array[leftpointer]
    array[leftpointer] = array[i-1]
    array[i-1] = leftdata
    return i - 1 



def quicksort_median(array, l_index, r_index):
    
    if l_index < r_index:
        temp_median = medianofthree_partitioning(array, l_index, r_index)
        quicksort_median(array, l_index, temp_median)
        quicksort_median(array, temp_median + 1, r_index)



#print(test4)

#quicksort_median(test4, 0, len(test4))


#print(test4)


def data_generator_sorted(arg2):
    tempArray1 = np.arange(1,arg2 + 1)
    tempArray = tempArray1.tolist()
    
    return tempArray

def data_generator_random(arg2):
    tempArray1 = np.arange(1,arg2 + 1)
    np.random.shuffle(tempArray1)
    tempArray = tempArray1.tolist()
    
    return tempArray

def data_generator_constant(arg2):
    tempArray1 = np.zeros(arg2, dtype=int)
    tempArray = tempArray1.tolist()
    
    return tempArray

t1 = time.perf_counter()

if (arg3 =='s'):
    data = data_generator_sorted(arg2)
    def helper(data):
        if(arg1 == 'q'):
            quicksort_median(data, 0, len(data))
        elif(arg1 == 's'):
            selectionSort(data, len(data))
        elif(arg1 == 'i'):
            insertionSort(data, len(data))
    helper(data)
    

elif (arg3 =='c'):
    data = data_generator_constant(arg2)
   # print(data)
    def helper(data):
        if(arg1 == 'q'):
            quicksort_median(data, 0, len(data))
        elif(arg1 == 's'):
            selectionSort(data, len(data))
        elif(arg1 == 'i'):
            insertionSort(data, len(data))
    helper(data)

elif(arg3 =='r'):
    data = data_generator_random(arg2)
    def helper(data):
        if(arg1 == 'q'):
            quicksort_median(data, 0, len(data))
        elif(arg1 == 's'):
            selectionSort(data, len(data))
        elif(arg1 == 'i'):
            insertionSort(data, len(data))
    helper(data)



#print(data)

print(" for " +arg1+ " of "+str(len(data))+ " in " +arg3+ " elements")

t2 = time.perf_counter()
print(f"Program execution {t2 - t1:0.15f} seconds")
def is_Sorted():
    i = 1
    flag = 0
    while i < len(data): 
        if(data[i] < data[i - 1]): 
            flag=1
        i += 1


    if (not flag) : 
        print ("Array is sorted.") 
    else : 
        print ("Array is not sorted.")

#print(data)
is_Sorted()