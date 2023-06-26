#1- Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário e calcule o total em segundos.

dia = int(input("Dia(s):"))
hora = int(input("Hora(s):"))
minuto = int(input("Minuto(s):"))
segundo = int(input("Segundo(s):"))
print(f"{dia} dia(s), {hora} hora(s), {minuto} minuto(s) e {segundo} segundo(s)")
dia = dia * 86400
hora = hora * 3600
minuto = minuto * 60
segundo = segundo + minuto + hora + dia
print(f"Equivale a {segundo} segundo(s)")