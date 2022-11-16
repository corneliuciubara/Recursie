def cmmdc(m, n):
    if m > n:
        return cmmdc(m-n, n)
    if m == n:
        return m
    else:
        return cmmdc(m, n-m)

m = int(input("m = "))
n = int(input("n = "))
print(cmmdc(m,n))