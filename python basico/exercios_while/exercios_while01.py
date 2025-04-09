# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.

numero = 4(int(input("Digite um número: ")))
fatorial = numero

while numero >= 2:
    fatorial = fatorial * (numero - 1)
    numero -= 1 #numero = numero - 1
print(fatorial)
