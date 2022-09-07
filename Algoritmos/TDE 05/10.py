a = int(input("Insira sua conta:"))
b = float(input("Qual seu saldo?"))

print("--------------------------------")

if b<0:
    print(f'A conta {a} está ESTOURADA')
else:
    print(f'A conta {a} está NORMAL')
