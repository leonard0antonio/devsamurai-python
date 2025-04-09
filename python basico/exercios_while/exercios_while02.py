# O programa deve solicitar ao usuário que digite uma senha de quatro dígitos numéricos. O usuário tem 3 tentativas para acertar a senha. Se o usuário acertar a senha, o programa deve exibir a mensagem "Acesso permitido". Se o usuário errar a senha, o programa deve exibir a mensagem "Senha incorreta, tente novamente" e permitir que o usuário tente novamente. Se o usuário errar a senha 3 vezes, o programa deve exibir a mensagem "Número máximo de tentativas excedido. Acesso bloqueado."

senha = '1222'
tentativas = 3

while tentativas > 0:
    entrada = input('Digite a senha de quatro dígitos numéricos: ')  # Entrada do usuário

    if entrada == senha:
        print('Acesso permitido')
        break
    else:
        tentativas -= 1  # Reduz uma tentativa
        print('Senha incorreta, tente novamente')

    print(f'Tentativas restantes: {tentativas}')

if tentativas == 0:
    print('Número máximo de tentativas excedido. Acesso bloqueado.')
