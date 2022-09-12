# A python program to find a peak element 
# Two methods: 1 Naive approach(return list of peak element index)
# 2: efficient approach- divide and conquer strategy()

import numpy as np

# Method1: naive approach
def find_peak_index_in_array(sample_array):  
    """
    finds and returns the list of index of all the peak elements in the sample array(1D) passed as an arguments using 
    naive approach
    
    Arguments:
    sample_array: sample array from which index of peak elements to be extracted
    
    Returns:
    peak_index_list: List containing index of all the peak elements in sample array
    """
    arr_len = sample_array.shape[0]
    peak_index_list = []

    # extract peak index if peak element is first and last element of array
    if sample_array[0]>sample_array[1]:
        peak_index_list.append(0)
    elif sample_array[arr_len-1]>sample_array[arr_len-2]:
        peak_index_list.append(arr_len-1)

    for index in range(1, arr_len-1):
        if (sample_array[index]>=sample_array[index-1] and sample_array[index]>=sample_array[index+1]):
            peak_index_list.append(index)
    return peak_index_list

# Method2: divide and conquer strategy
def find_peak_divide_conquer(arr, low, high, n):
    """
    Returns a peak element from the input array passed as an argument with the technique of divide and conquer 
    recursively (i.e. calling the same function multiple times.)
    
    Arguments:
    arr: sample array, 1D numpy array
    low: index of first element of array
    high: index of last element of array
    n: number of elements in the array, length of 1D array
    
    Return:
    a peak element from an input array
    """
    # Find index of middile element i.e. (low+high)/2
    mid = low+(high-low)/2
    mid = int(mid)
    
    # Compare middle element with its neighbours (if neighbour exists)
    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])): 
        return mid
    # If middle element is not peak and its left neighbour is greater than it, then left half must have a peak
    elif(mid>0 and arr[mid-1]>arr[mid]):
        return find_peak_divide_conquer(array, low, (mid-1), n)
    
    # If middle element is not peak and its right neighbour is greater than it, the right half must have a peak
    else:
        return find_peak_divide_conquer(array, (mid+1), high, n)
    
# Define rapper over recursive function find_peak_divide_conquer()
def find_peak(array, n):
    return find_peak_divide_conquer(array, 0, n-1, n)

# Sample array 
array = np.array([10, 20, 15, 2, 23, 90, 67])

# Method1: naive approach
peak_index_list = find_peak_index_in_array(array)
print(f"List of all the index of peak elements in array {array} using naive approach is\are:\n {peak_index_list}")

# Method2: divide and conquer strategy
n = array.shape[0]
print("\nIndex of a peak point using divide and conquer strategy is: ", find_peak(array, n))