arr = [5,2,8,1]


def insertion_sort(arr,n):
    if n <= 1:
        return
    insertion_sort(arr,n-1)
    key = arr[n-1]
    i = n-2
    while i <= 0 and arr[i]> key:
        arr[i+1] = arr[i]
        i-=1
    arr[i+1]=key

insertion_sort(arr,len(arr))
print(arr)