# count sort is a index based sort.
# counting the elements having distint key values.
# we take another array with size is equal to max value of elements to store the count of item.


def countsort(A):
    l=len(A)
    m=max(A)
    carray=[0]*(m+1)
    for i in range(l):
        # print(A[i],carray[A[i]])
        carray[A[i]]+=1
    print(carray)
    i=0
    j=0
    while i<(m+1):
        if carray[i]>0:
            A[j]=i
            j+=1
            carray[i]-=1
        else:
            i+=1



A=[1,2,3,4,2,3,1,3]
print("original :",A)
countsort(A)
print("sorted :",A)


