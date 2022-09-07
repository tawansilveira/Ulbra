import random

def rolar_Dados(tamanho):
    return random.randint(1, tamanho)

a = input(' ')
b = a.split('d')

for i in range(int(b[0])):
    res = rolar_Dados(int(b[1]))
    print(f'Dado {i+1}: {res}')

