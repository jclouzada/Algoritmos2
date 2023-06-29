import sys
print(f"Número de parâmetros: {len(sys.argv)}")
for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo. readlines ():
        print(linha)