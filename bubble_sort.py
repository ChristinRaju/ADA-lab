def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


nums = [37, 45, 29, 8, 12]
print("Original array:", nums)
print("Sorted array:", bubble_sort(nums))
