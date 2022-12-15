def rec(n):
    if n==1:
        return 1
    else:
        print(n)
        return rec(n-1)

k=rec(10)
print("vn")
print(k)