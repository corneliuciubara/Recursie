def aputerebiterare(a, b):
    p = 1
    for i in range(0, b):
        p = p*a
    for i in range(b, 0):
        p = p / a
    return p

def aputerebrecursie(a, b):
    if b > 0:
        return (a * aputerebrecursie(a, b-1))
    elif b < 0:
        return (1 / a * aputerebrecursie(a, b+1))
    else :
        return 1

lst = [(1, 2), (2, -2), (3, 4), (4, 0), (-1, 3), (4, -2), (1, 3), (4, 5), (3, 4), (2, -1), (-1, 4), (-2, -4)]

for (a,b) in lst:
    print("Iterare : ", a,"**",b," = ",aputerebiterare(a, b))
    print("Recursie: ", a,"**",b," = ",aputerebrecursie(a, b))
