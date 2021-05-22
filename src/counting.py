def counting(arr):
 
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]
 
    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]
 
    # For storing the resulting answer since the 
    # string is immutable
    ans = ["" for _ in arr]
 
    # Store count of each character
    for i in arr:
        count[ord(i)] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i-1]
 
    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
 
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans

# Python program for implementation of Bubble Sort 
  
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr
 
 
 def selectionsort(arr):
    for i in range(len(arr)):
      
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if A[min_idx] > arr[j]:
                min_idx = j
              
        # Swap the found minimum element with 
        # the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
        
def shellSort(arr):
    gap = len(arr) // 2 # intiliaze the gap
 
    while gap > 0:
        i = 0
        j = gap
         
        # check the array in from left to right
        # till the last possible index of j
        while j < len(arr):
     
            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
             
            i += 1
            j += 1
         
        # now we cannot move towards left anymore so
        # check the element from last index of i towards to left side of the array
        while i - gap != -1:
 
            if arr[i - gap] > arr[i]:
                arr[i-gap],arr[i] = arr[i],arr[i-gap]
            i -= 1
 
        gap //= 2
    return arr
