# Exercício 2: Crie uma função que converta uma temperatura em Fahrenheit para Celsius. A fórmula de conversão é: C = (F - 32) * 5/9.

def temperatura (temp):
    #
    celcius = (temp - 32) * 5 / 9
    return celcius

print("a temperatura em Celsius é: ", temperatura(32))