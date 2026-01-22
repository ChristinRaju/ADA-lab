import random

nums = [random.randint(1, 100) for _ in range(5)]

def selection_sort(arr):
    arr = arr.copy()  
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print("Original array:", nums)
print("Sorted array:", selection_sort(nums))
