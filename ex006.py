# 6 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
import defs04
def gerarlista(L1,L3):
    L3.append(int(L1[0]))
    n=(int(0))
    for i in range(len(L1)):
        for j in range(len(L3)):
            if L1[i] == L3[j]:
                n = 1
       if n == 1:
           L3.append(int(L1[i]))
    """for i in range(len(L2)):
        for j in range(len(L3)):
            if L2[i] != L3[j]:
                L3.append(int(L2[i]))"""
    return L3


tam1 = int(input("Digite o tamanho da primeira lista "))
tam2 = int(input("Digite o tamanho da segunda lista "))
L1 = []
L2 = []
L3 = []
defs04.lista(L1, tam1)
defs04.lista(L2, tam2)
print(gerarlista(L1, L3))
