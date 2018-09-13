# a regular comb sort algorithm is unnecessary because we know
# where every element has to go to (because the element is its absolute)
# position in the array

def minimumSwaps(arr):
    swaps = 0
    
    for i in range(len(arr)):
        while (arr[i] != i+1):
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            swaps += 1
            
    return swaps
