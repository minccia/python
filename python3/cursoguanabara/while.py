#sexo = str(input(
#                     'Qual é o seu sexo? [M/F] '
#    )).strip().capitalize()
#
#while sexo not in 'MFfm':
#    sexo = (str(input(
#                        'Sexo inválido, por favor insira um válido. [M/F] '))).strip().upper()
#
#print('Seu sexo foi registrado com sucesso.')
#
#from random import randint
#
#print(
#        'Este é o jogo da adivinhação! Eu vou pensar em um número aleatório entre 0 e 10, e você tenta adivinhar. Tudo bem?') 
#    
#num = int(input((
#                    'Escolha um número: '
#                )))
#
#computer_num = randint(0, 10)
#
#tentativas = 1
#while num != computer_num:
#
#    num = int(input(
#                        'Parece que você errou! Tente outro número: '))
#    tentativas += 1
#
#print(
#        'Parabéns, você acertou! Eu pensei no número {}. O seu número de tentativas foi: {}'.format
#        (computer_num, tentativas))
#
#if tentativas > 10:
#    print(
#            'Você tentou mais de 10 vezes, como você é burra, cara! Que loucura.')
#
#n1 = int(input(
#                'Digite um valor: '
#        ))
#n2 = int(input(
#                'Digite um outro valor: '
#        ))
#
#print("""Operações disponíveis:
#        [1] Soma
#        [2] Multipicação
#        [3] Definir o maior
#        [4] Inserir novos números
#        [5] Sair do programa""")
#
#pointer = 0
#while pointer != 5:
#    pointer = int(input(
#                        'Digite o número da operação que deseja realizar: '
#            ))
#    if pointer == 1:
#        print(
#                'A soma dos números dados é: {}'.format(n1
#                                                        + n2)
#        )
#    elif pointer == 2:
#        print(
#                'A multiplicação dos números dados é: {}'.format(n1
#                                                                 * n2)
#        )
#    elif pointer == 3:
#        if n1 > n2:
#            print(
#                    'O maior número é: {}'.format(n1)
#          )
#        elif n2 > n1:
#            print(
#                    'O maior número é: {}'.format(n2)
#            )
#        elif n1 == n2:
#            print(
#                    'Os números são iguais, portanto não há um maior.'
#            )
#    elif pointer == 4:
#        n1 = int(input(
#                'Digite um valor: '
#        ))
#        n2 = int(input(
#                'Digite um outro valor: '
#        ))
#
#print('Fim.')

# Lê um número qualquer e mostra o seu fatorial

#num = int(input(
#                    'Digite um número para ver o seu fatorial: '
#                ))
#
#antecessor = num - 1
#fatorial = num * antecessor
#
#while antecessor > 1:
#    num -= 1
#    antecessor -= 1
#    fatorial *= antecessor
#
#print(
#        'O número escolhido foi {} e o seu fatorial é {}'.format(num, fatorial)
##    )
#
#primeiro_termo = int(input(
#                                'Qual é o primeiro termo da P.A? '
#))
#
#razao = int(input(
#                                'Qual é a razão? '
#))
#
#indice = 1
#termo = primeiro_termo
#total = 0
#mais = 10
#print('Os dez primeiros termos da P.A são:')
#
#while mais != 0:
#    total += mais
#    while indice <= total:
#        print('{} > '.format(termo), end ='')
#        indice += 1
#        termo += razao
#    print('Pit-stop')
#    mais = int(input('Quantos termos você quer mostrar a mais? '))
#
#print('E morreu, acabou!')
#print("({},".format(primeiro_termo), end = '') 
#while indice > 0:
#    indice -= 1
#    termos += razao
#    print(" {},".format(termos), end = '')

#print(")", end='')

# Sequência de Fibonacci

#numero_de_termos = int(input(
#                                'Quantos termos da sequência de fibonacci você deseja ver? '
#))
#
#indice = 3
#primeiro = 0
#segundo = 1
#
#print('{} > {}'.format(primeiro, segundo), end = '')
#while indice <= numero_de_termos:
#    termo_seguinte = primeiro + segundo
#    print(' > {} >'.format(termo_seguinte), end = '')
#    primeiro = segundo
#    segundo = termo_seguinte
#    indice += 1
#

#numeros = soma = 0
#numeros = int(input(
#                    'Digite um número [999 para parar] '
#))
#while numeros <= 998:
#    soma += numeros
#    numeros = int(input(
#                    'Digite um número [999 para parar] '
#                ))
#if numeros == 999:
#    print('Acabou')
#
#print(
#        'A soma de todos os números foi: {}'.format(soma)
#    )
#
#
#numeros = soma = média = maior = menor = 0
#contador = 1
#disagree = 0
#while contador != 0 and disagree == 0:
#    numeros = int(input('Digite um número: '))
#    prosseguir = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
#    if prosseguir == 'S':
#        contador += 1
#        soma = numeros + numeros
#        média = float(soma / contador)
#
#        if contador == 1:
#            maior = menor = numeros
#
#        elif numeros > maior:
#            maior = numeros
#
#        elif numeros < menor:
#            menor = numeros
#
#    elif prosseguir == 'N':
#        disagree = 1
#        print('Acabou')
#    else:
#        disagree = 1
#        print('Inválido')
#
#print(
#"""Você digitou {} números, a soma entre eles foi {}
#e a média entre eles foi {}. O maior é {} e o menor é {}""".format(
#contador, soma, média, maior, menor), end = ''
#     )

primeiro_termo = int(input('Qual é o primeiro termo da razão? '))

razao = int(input('Qual é a razão? '))

print('Os dez primeiros termos da P.A são:')
print('{} > '.format(primeiro_termo), end = '')

for progressao in range(0, 9):
    termos = primeiro_termo + razao
    primeiro_termo = termos
    print('{} > '.format(termos), end = '')