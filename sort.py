def sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


arr = [9,1,2,3,4,7,8,]
sort(arr)
print('sorted array:', arr)
