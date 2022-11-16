n=int(input("Dati numarul de elemente din tablou unidimensional = "))
z=[]

print("Introduceti ",n ," elemente pentru tabloul unidimensional creat")
for i in range(0, n):
    x=int(input('elementul z[' +str(i)+']='))
    z.append(x)
print("Tabloul unidimensional obtinut: ", z)

print("a) Tabloul unidimensional in ordinea citirii lor: ", z)

b=z[0:]
b.reverse()
print("b) Elementele tabloului unidimensional in ordine inversa: ", b)

print("c) Suma elementelor tabloului: ", sum(z))

s1 = 0
for i in z:
    if not i%2:
        s1 += i 
print("d) Suma componentelor pare: ", s1)

def sumimp(z):
    return sum([i for i in z if i%2 == 1])
print("e) Suma elemetelor impare: ", sumimp(z))


d=[]
for i in range(0,len(z)):
    if z[i]%2==0:
        d.append(z[i])
print("f) Elementele pare", d)

f=[]
for i in range(0,len(z)):
    if z[i]%2==1:
        f.append(z[i])
print("g) Elementele impare: ",f) 

