# Exercício 1: Faça um programa que peça ao usuário para digitar duas notas, calcule a média e informe se o aluno foi aprovado, reprovado ou está de recuperação. Considere que a média para aprovação é 7.0 e para recuperação é entre 5.0 e 6.9.

nota1 = eval(input("escreva a primeira nota: "))
nota2 = eval(input("escreva a segunda nota: "))

media = (nota1 + nota2 ) / 2

print(media)

if media >= 7.0:
  print("aluno aprovado")
elif media >= 5 and media < 7:
   print("você estar de recuperação")
else:
   print("aluno reprovado")
