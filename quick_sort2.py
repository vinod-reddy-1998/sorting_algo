def quicksort(A,low,high):
    if low<high:
        loc=partition(A,low,high)
        quicksort(A,low,loc-1)
        quicksort(A,loc+1,high)



def partition(A,low,high):
    pivot=A[low]
    i=low+1
    j=high
    while True:
        while i<=j and A[i]<=pivot:
            i+=1
        while i<=j and A[j]>=pivot:
            j-=1
        if i<=j:
            A[i],A[j]=A[j],A[i]
        else:
            break
    A[low],A[j]=A[j],A[low]
    return j

A=[3,5,8,9,6,3]
print("original",A)
quicksort(A,0,len(A)-1)
print("sorted",A)