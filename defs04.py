def lista(L,tam):
    for i in range(tam):
        L.append(int(input(f"Digite o {i+1}º número da lista")))
"""
    for i in range(tam):
        print(L[i])
"""


def maiorNum(L):
    maiorNum = L[0]
    i=1
    while i != (len(L)):
        if maiorNum<L[i]:
            maiorNum=L[i]
        i= i+1
    return maiorNum


def menorNum(L):
    menorNum = L[0]
    i=1
    while i != (len(L)):
        if menorNum>L[i]:
            menorNum=L[i]
        i= i+1
    return menorNum

def media(L):
    soma = 0
    for i in range(len(L)):
        soma = L[i]+soma
    valorMedio = soma/(len(L))
    return valorMedio


def gerarlista(L1,L3):
    L3.append(int(L1[0]))
    n=(int(0))
    for i in range(len(L1)):
        for j in range(len(L3)):
            if L1[i] == L3[j]:
                n=1
            else:
                pass
       if n == 1:
           L3.append(int(L1[i]))
    """for i in range(len(L2)):
        for j in range(len(L3)):
            if L2[i] != L3[j]:
                L3.append(int(L2[i]))"""
    return L3

