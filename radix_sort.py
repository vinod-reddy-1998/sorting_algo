def radixsort(A):
    l=len(A)
    maxelement=max(A)
    digits=len(str(maxelement))
    a=[]
    bins=[a]*10
    for i in range(digits):
        for j in range(l):
            e=int(A[j]/pow(10,i))%10
            if len(bins[e])>0:
                bins[e].append(A[j])
            else:
                bins[e]=[A[j]]
        k=0
        print("bins",bins)
        for x in range(10):
            if len(bins[x])>0:
                for y in range(len(bins[x])):
                    A[k]=bins[x].pop(0)
                    k=k+1


A=[23,45,564,28,976,1,234]
print("original",A)
radixsort(A)
print("sorted",A)

 