"""#7- Crie um programa que inverta a ordem das linhas do arquivo pares.txt. A primeira linha deve conter o maior número; e a última, o menor.
import sys"""
with open("pares.txt","w") as pares:
    for n in range(0,11):
        if n%2 ==0:
            pares.write(f"{n}\n")
with open("pares.txt","r") as pares:
    conteudo = pares.readlines()
with open("pares.txt","w") as decrepares:
    for linha in conteudo[::-1]:
        decrepares.write(linha)
        print(linha)
