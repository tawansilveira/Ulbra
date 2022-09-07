a = int(input("Insira um número:"))
b = int(input("Insira outro número:"))
c = a%2
d = b%2

if c == 0:
    print(f'{a} é múltiplo de 2')
else:
    print(f'{a} não é múltiplo de 2')

if d == 0:
    print(f'{b} é múltiplo de 2')
else:
    print(f'{b} não é múltiplo de 2')