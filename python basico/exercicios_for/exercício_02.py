# O programa deve solicitar ao usuário que digite um número inteiro positivo n. O programa deve calcular o n-ésimo número da sequência de Fibonacci, onde os dois primeiros números são 1 e 1, e cada número subsequente é a soma dos dois anteriores.

n = int(input("Digite qual elemento da sequência de Fibonacci você deseja: "))
primeiro = 1
segundo = 1

if n == 1 or n == 2:
    print("O número é 1")
else:
    for _ in range(2,n):
        terceiro = primeiro + segundo
        primeiro = segundo
        segundo = terceiro
    print("O número é: ", terceiro)

