#n is the size of heap
def max_heapify(arr,n,i):
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[l]>arr[i]:
        largest = l
    else:
        largest = i
    if r<n and arr[r]>arr[largest]:
        largest = r
    if largest!=i:
        arr[i],arr[largest] = arr[largest],arr[i]
        max_heapify(arr,n,largest)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2-1,0,-1):
        max_heapify(arr,n,i)

def heapSort(arr):
    build_max_heap(arr)
    n = len(arr)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        max_heapify(arr,i,0)

# Driver code to test above
arr = [ 100,20,30,10,15,7,14]
heapSort(arr)
n = len(arr)
print ("Sorted array is",arr)