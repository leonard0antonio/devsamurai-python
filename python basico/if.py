# Exercicio 1
# O programa deve solicitar ao usuário que digite uma temperatura em graus Celsius. O programa deve exibir uma mensagem indicando se a temperatura está quente (acima de 30 graus), agradável (entre 20 e 30 graus) ou fria (abaixo de 20 graus).

temp = eval(input("digite a temperatura nesse momento: "))
if temp >= 40:
  print("estar muito calor")
elif temp > 30:
  print("estar agradavel")
else:
  print("estar frio") 