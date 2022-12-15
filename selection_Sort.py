# it is unstable sorting algo.
# true position of the array is changed.

# select the minimum element from the list.
# place selected element at its exact position.
# apply this technique on all the elements.

# sorts from the start index...



def selectionsort(A):
    l=len(A)
    for i in range(0,l-1):
        min=i
        for j in range(i+1,l):
            if A[j]<A[min]:
                min=j
        tmp=A[i]
        A[i]=A[min]
        A[min]=tmp

A=[3,5,7,2,1,8]
print("original:",A)

selectionsort(A)
print("sorted:",A)