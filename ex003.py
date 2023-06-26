"""3- Escreva um programa que pergunte a distância que um passageiro deseja percorrer em
km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200 km, e
R$ 0,45 para viagens para longas."""

km = int(input("Digite a distância da viagem "))
if km > 200:
    km = km * 0.45
else:
    km = km * 0.5
print(f"O valor da passagem é: {km}")