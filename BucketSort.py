def bucketSort(arr):
    new_arr = []
    buckets = 10 # hardcoded
    for i in range(buckets):
        new_arr.append([])

    #putting in respective buckets
    for j in arr:
        index = int(buckets*j)
        new_arr[index].append(j)
    #individual sorting inside the buckets
    for i in range(len(arr)):
        new_arr[i]=insertionSort(new_arr[i])

    #concatenate the results
    k = 0
    for i in range(buckets):
        for j in range(len(new_arr[i])):
            arr[k]=new_arr[i][j]
            k=k+1
    return arr

def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while(i>=0 and arr[i]>=key):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
    return arr

# Driver Code
x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))