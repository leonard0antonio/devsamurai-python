# Crie um programa que solicite ao usuário um número e exiba a tabuada desse número até um limite definido pelo usuário.

tabuada = int(input("Digite um número para ver a tabuada: "))
limite = int(input("Digite o limite da tabuada: "))

for numero in range(0, limite + 1):
    resultado = tabuada * numero
    print(f"{tabuada} x {numero} = {resultado}")  