def calculo(comando,numero):
  if comando == 'quadrado':
    return numero * numero
  else:
    return numero * numero * numero
  
print(calculo('cubo', 2))
print(calculo('quadrado', 3))
