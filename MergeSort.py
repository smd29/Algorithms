def merge(arr,p,q,r):
    n1=q-p+1
    n2=r-q
    left_array = []
    right_array = []
    for i in range(0,n1):
        left_array.append(arr[p+i])
    for i in range(0,n2):
        right_array.append(arr[q+1+i])
    left_array.append(999) #considering 999 is the largest no
    right_array.append(999)

    i = 0
    j = 0
    for k in range(p,r+1):
        if(left_array[i]<=right_array[j]):
            arr[k]=left_array[i]
            i = i+1
        else:
            arr[k]=right_array[j]
            j = j+1


#code for merge
def mergeSort(arr,p,r):
    if(p<r):
        q = (p+r-1)//2
        mergeSort(arr,p,q)
        mergeSort(arr,q+1,r)
        merge(arr, p, q, r)


# Driver code to test above
arr = [1,5,7,8,2,4,6,9]
print(arr)
n = len(arr)
print("after sorting")
mergeSort(arr,0,n-1)
print(arr)