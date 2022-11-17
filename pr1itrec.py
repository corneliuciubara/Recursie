print("Iterativ: ")
def sumaiterativa1(n):
    s1 = 0
    for i in range(1, n*2*(n - 1)):
        s1 += i
    return s1
n1 = int(input("a) n1 = "))
print("a) ", sumaiterativa1(n1))

print("\n")

def sumaiterativa2(n):
    s2 = 0
    for i in range(1, n/(((2*n)-1)*((2*n)+1))):
        s2 += i
    return s2
n2 = int(input("b) n2 = "))
print("b) ", sumaiterativa2(n2))

print("\n")

print("Recursiv: ")
def sumarecursiva1(n):
    if (n > 1):
        return n + sumarecursiva1(n*2*(n-1))
    else:
        return n
n3 = int(input("a) n3 = "))
print("a) ", sumarecursiva1(n3))

print("\n")

def sumarecursiva1(n):
    if (n > 1):
        return n + sumarecursiva1(n/(((2*n)-1)*((2*n)+1)))
    else:
        return n
n4 = int(input("b) n4 = "))
print("b) ", sumarecursiva1(n4))

