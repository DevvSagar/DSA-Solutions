arr = [5,2,8,1]
def one_pass(arr,n,i):
    if i == n-1:
        return
    if arr[i] > arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
    one_pass(arr,n,i+1)



def bubble_sort(arr,n):
    if n == 1:
        return
    one_pass(arr,n,0)
    bubble_sort(arr,n-1)



bubble_sort(arr,len(arr))
print(arr)