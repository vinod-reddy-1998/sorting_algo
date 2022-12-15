def bubbleSort(A):
    l=len(A)
    for i in range(l):
        for j in range(l-i-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    


A=[3,5,7,2,1,8]
print("original:",A)

bubbleSort(A)
print("sorted:",A)
