# 6 - Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
import defs04


tam1 = int(input("Digite o tamanho da primeira lista "))
tam2 = int(input("Digite o tamanho da segunda lista "))
L1 = []
L2 = []
L3 = []
defs04.lista(L1, tam1)
defs04.lista(L2, tam2)
print(defs04.gerarlista(L1,L2,L3))
