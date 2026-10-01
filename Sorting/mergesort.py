arr = [8, 3, 5, 4, 7, 6, 1, 2]

def merge(arr,left,mid,right):
    result = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            result.append(arr[i])
            i+=1
        else:
            result.append(arr[j])
            j+=1
    while i <= mid:
        result.append(arr[i])
        i+=1
    while j <= right:
        result.append(arr[j])
        j+=1
    for k in range(len(result)):
        arr[left + k] = result[k]
    return arr



def merge_sort(arr,left,right):
    if left >= right:
        return arr

    mid = (left+right) // 2
    merge_sort(arr,left,mid)
    merge_sort(arr,mid+1,right)
    merge(arr,left,mid,right)


merge_sort(arr,0,len(arr)-1)
print(arr)