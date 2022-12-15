# merge sort algo is based upon on divide and concur approach
# it always split in two halves.
def mergeSort(A,left,right):
    if left<right:
        mid=(left+right)//2
        mergeSort(A,left,mid)
        mergeSort(A,mid+1,right)
        merge(A,left,mid,right)

def merge(A,left,mid,right):
    i=left
    j=mid+1
    k=left
    B=[0]*(right+1)
    while i<=mid and j<=right:
        if A[i]<A[j]:
            B[k]=A[i]
            k+=1
            i+=1
        else:
             B[k]=A[j]
             k+=1
             j+=1
    while i<=mid:
        B[k]=A[i]
        i+=1
        k+=1
    while j<=right:
        B[k]=A[j]
        j+=1
        k+=1
    print(B)
    for x in range(left,right+1):
        A[x]=B[x]


A=[3,5,7,2,1,8]
print("original",A)
mergeSort(A,0,len(A)-1)
print("sorted",A)

    