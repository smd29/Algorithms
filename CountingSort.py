def countingSort(arr,upper_range):
    cells = upper_range+1
    count = [0]*cells
    for i in arr:
        count[i]+=1
    i = 0
    for j in range(cells):
        for k in range(count[j]):
            arr[i]=j
            i=i+1
    return arr

# Driver code to test above
arr = [10, 7, 8, 9, 1, 5,10,7,5,5]
print("before sorting")
print(arr)
print("after sorting")
countingSort(arr,10)
print(arr)