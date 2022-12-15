def selectionsort(A):
    l=len(A)
    for i in range(0,l-1):
        pos=i
        for j in range(i+1,l):
            if A[j]<A[pos]:
                pos=j
        tmp=A[i]
        A[i]=A[pos]
        A[pos]=tmp

A=[3,5,7,2,1,8]
print("original",A)

selectionsort(A)
print("sorted",A)