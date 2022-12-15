def shellSort(A):
    n=len(A)
    gap=n//2
    while gap>0:
        i=gap
        while i<n:
            temp=A[i]
            j=i-gap
            while j>=0 and A[j]>temp:
                A[j+gap]=A[j]
                j=j-gap
            A[j+gap]=temp
            i+=1
        gap=gap//2
A=[3,5,7,2,1,8]
print("original",A)

shellSort(A)
print("sorted",A)
