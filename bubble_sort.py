# it compares the consecutive elements.
# if left element is greater than right element swap them
# continue till the end of the collection.
 
def bubbleSort(A):
    n=len(A)
    for p in range(n-1,0,-1):
        for i in range(p):
            if A[i]>A[i+1]:
                temp=A[i]
                A[i]=A[i+1]
                A[i+1]=temp
A=[3,5,7,2,1,8]
print("original:",A)

bubbleSort(A)
print("sorted:",A)
