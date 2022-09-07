a = int(input("Insira um número:"))
b = int(input("Insira outro número:"))
c = int(input("Insira mais um número:"))

print("---------------------------------")
print("O maior valor é:")

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)