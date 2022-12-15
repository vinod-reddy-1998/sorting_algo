# time complexity of quick sort is 1+2+4+8+16.....
# which is log(n)


def partition(A,left,right):
    pivot=A[left]
    start=left
    end=right
    while start<end:
        while A[start]<=pivot:
            start+=1
        while A[end]>=pivot:
            end-=1
        if start<end:
            temp=A[start]
            A[start]=A[end]
            A[end]=temp
    temp=A[left]
    A[left]=A[end]
    A[end]=temp
    return end


def QuickSort(A,left,right):
    if left<right:
        loc=partition(A,left,right)
        QuickSort(A,left,(loc-1))
        QuickSort(A,(loc+1),right)


A=[3,5,7,2,1,8]
print("original",A)
l=len(A)-1
print(l)
QuickSort(A,0,l)
print("sorted",A)