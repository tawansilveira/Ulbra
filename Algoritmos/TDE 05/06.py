a = float(input("Digite um número:"))
b = float(input("Digite outro número:"))
c = float(input("Digite mais um número:"))

print("****************************************")

if a > 0:
    print("Raíz do primeiro número:")
    print(a**0.5)
else:
    print("Quadrado do primeiro número:")
    print(a**2)

print("****************************************")

if b > 10 and b < 100:
    print("VERIFICAÇÃO DO SEGUNDO NÚMERO")
    print("NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO")
else:
    print("VERIFICAÇÃO DO SEGUNDO NÚMERO")
    print("INTERVALO NÃO PERMITIDO")

print("****************************************")

if c < b:
    print("Subtração do segundo e do terceiro número")
    print(b - c)
else:
    print("Soma do segundo e do terceiro número")
    print(b + c)