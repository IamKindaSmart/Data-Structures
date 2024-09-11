def merge(arr,low,mid,high):
    c=[]
    start1=low
    start2=mid+1

    while start1 <= mid and start2 <= high:
        if arr[start1] < arr[start2]:
            c.append(arr[start1])
            start1 += 1
        else:
            c.append(arr[start2])
            start2 += 1

    while start1 <= mid:
        c.append(arr[start1])
        start1 += 1

    while start2 <= high:
        c.append(arr[start2])
        start2 += 1

    k=0
    for i in range(low,high+1):
        arr[i] =c[k]
        k += 1

def mergeSort(arr, low, high):
    if low < high:
        mid = (low+high) // 2  #// only use real whole integers (No rounding)
        mergeSort(arr, low, mid) #1st partition
        mergeSort(arr,mid+1,high) #2nd Partition
        merge(arr, low, mid, high) #combining the divided lists in sorted order

arr=[12,100,4,1,8]
n = len(arr)

mergeSort(arr,0,n-1)
print(arr)

