# select one element at a time from the left of the collection.
# insert the element at the proper position
# after insertion of the element to the left is sorted.


def insertionSort(A):
    l=len(A)
    for i in range(1,l):
        cvalue=A[i]
        pos=i
        while pos>0 and A[pos-1]>cvalue:
            A[pos]=A[pos-1]
            pos=pos-1
        A[pos]=cvalue

A=[3,5,7,2,1,8]
print("original:",A)

insertionSort(A)
print("sorted:",A)