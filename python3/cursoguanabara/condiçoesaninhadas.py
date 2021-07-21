#nome = str(input("Qual é seu nome? ")).strip().title()
#
#print('-------------------------------- CARREGANDO --------------------------------------------------')
#
#if nome == "Luísa":
#    print("Nossa que nomão querida, ulalá")
#
#elif nome in "Le" or "Luíse":
#    print('omg é Le Luíse!!!!!')
#
#print("Bom dia, {}!".format(nome))

# Aprovando empréstimo bancário

#casa = int(input('Qual é o valor da casa? ')) # Lê o valor da casa
#salario = int(input('Qual é o valor do seu salário? ')) # Lê o salário do comprador
#ano = int(input('Em quantos anos você pretende pagar? '))*12 # Lê o número de anos em que a pessoa pretende pagar e converte em meses
#
#if casa/ano > (salario*30)/100:
#    print('Sentimos muito, mas o seu empreśtimo foi negado.')
#
#else:
#    print('Parabéns, o empréstimo foi aceito. ')

##Calculadora de binário, octal e hexadecimal
#numero = int(input("Digite um número inteiro qualquer: "))
#
#print("")
#
#base = str(input(
#                   """Qual será a base de conversão? \033[0;33;1m \n
#1. Binário \033[m \n \033[0;32;1m 
#2. Octal \033[m \n \033[0;31;1m
#3. Hexadecimal \033[m \n 
#Digite aqui: """
#                                                       )).strip().capitalize()
#
#
#if base == 'Octal':
#    print('O número escolhido foi {}, em octal ele fica: {}'.format(numero, oct(numero)[2:]))
#
#elif base == 'Binario' or base == 'Binário':
#    print('O número escolhido foi {}, em binário ele fica: {}'.format(numero, bin(numero)[2:]))
#
#elif base == 'Hexadecimal': 
#    print('O número escolhido foi {}, em hexadecimal ele fica {}'.format(numero, hex(numero)[2:]))

#Comparando números

#n1 = int(input(
#                'Digite um número: ')) # Lê um número inteiro qualquer
#
#n2 = int(input(
#                'Digite outro número: ')) # Lê um outro número inteiro qualquer
#
#if n1 > n2:
#    print(
#            'O \033[0;33;1m primeiro \033[m valor é maior') # Determina que o primeiro valor é maior.
#
#elif n2 > n1:
#    print(
#            'O \033[0;31;1m segundo \033[m valor é maior') # Determina que o segundo valor é maior.
#
#elif n1 == n2:
#    print(
#            '\033[0;32;1m Não existe valor maior, os números são iguais. \033[m') # Printa que os números
#                                                                                  # são iguais
#
## Alistamento militar
#
#idade = 2022 - int(input(
#                        'Em que ano você nasceu? '))
#
#if idade < 18:
#    alistamento = 18 - idade
#    print(
#            """Ainda não chegou o momento de você se alistar, faltam \033[0;33;1m{}\033[m anos.""".format(alistamento)
#      )
#
#elif idade == 18:
#    print(
#            """Você possui\033[0;33;1m 18 anos\033[m, portanto, é o seu ano de se alistar."""
#     )
#
#elif idade > 18:
#    alistamento = idade - 18
#    print(
#            """Você possui \033[0;33;1mmais de 18 anos\033[m e o seu alistamento está atrasado a \033[0;32;1m{} \033[manos.""".format(alistamento)
#    )

# Média das notas de um aluno
#
#m1 = float(input(
#                    'Digite a sua primeira nota: '))
#m2 = float(input(
#                    'Digite a sua segunda nota: '))
#
#media = (m1+m2)/2
#
#if media <= 5.0:
#    print(
#            'Sua média foi {}, logo você está REPROVADO.'.format(media)
#    )
#
#elif media > 5.0 and media <= 6.9:
#    print(
#            'Sua média foi {}, portanto você está de recuperação.'.format(media)
#    )
#
#elif media >= 7.0:
#    print(
#            'Sua média foi {}, logo você foi APROVADO'.format(media)
#    )

# Natação
#
#
#idade = int(input(
#
#                    'Qual é a idade do atleta? '
#
#        ))
#
#
#if idade <= 9:
#
#    print(
#
#            'Este atleta possui {} anos de idade, portanto é um atleta MIRIM'.format(idade)
#
#        )
#
#
#elif idade > 9 and idade <= 14:
#
#    print(
#
#            'Este atleta possui {} anos de idade, portanto é um atleta INFANTIL'.format(idade)
#
#        )
#
#
#elif idade > 14 and idade <= 19:
#
#    print(
#
#            'Este atleta possui {} anos, portanto é um atleta JUNIOR'.format(idade)
#
#    )
#
#
#elif idade > 19 and idade <= 20:
#
#    print(
#
#            'Este atleta possui {} anos, portanto é um atleta SÊNIOR'.format(idade)
#
#    )
#
#
#elif idade > 20:
#
#    print(
#
#            'Este atleta possui {} anos de idade, portanto é um atleta MASTER'.format(idade)
#
#    )

# Triângulo aprimorado
#
#r1 = int(input(
#                'Me dê o valor em centímetros de uma reta '
#        ))
#r2 = int(input(
#                'Me dê o valor em centímetros de uma outra reta '
#        ))
#r3 = int(input(
#                'Me dê o valor em centímetros de mais uma reta '
#        ))
#
#print(
#        '\033[0;33;40mÉ possível formar um triângulo com estas três retas?\033[m '
#    )
#
#absolute = r2-r3 
#soma = r2 + r3
#
#if absolute < r1 < soma:
#    print(
#            'Sim, é possível formar um triângulo com estas três retas'
#        )
#
#    if r1 == r2 and r2 == r3:
#        print(
#                'Este triângulo é equilátero, pois possui todos os lados iguais.'
#        )
#
#    elif r1 == r2 and r2 != r3 or r2 == r3 and r2 != r1:
#        print(
#                'Este triângulo é isósceles, pois possui dois lados iguais.'
#        )    
#
#    elif r1 != r2 and r2 != r3:
#        print(
#                'Este triângulo é escaleno, pois possui todos os lados diferentes.'
#        )
#else:
#    print(
#            'Não é possível formar um triângulo com estas três retas'
#        )

# Calculando o IMC
#
#alt = float(input(
#                    'Digite a sua altura: '
#))**2
#
#pes = float(input(
#                    'Digite o seu peso: '
#))
#
#imc = pes/alt
#
#if imc <= 18.5:
#    print(
#            'Seu IMC é: {:.1f} e você está abaixo do peso ideal.'.format(imc)
#    )
#
#elif imc > 18.5 and imc <= 25:
#    print(
#            'Seu IMC é: {:.1f} e você se encontra no seu peso ideal.'.format(imc)
#    )
#elif imc > 25 <= 30:
#    print(
#            'Seu IMC é: {:.1f} e você se encontra com sobrepeso.'.format(imc)
#    )
#elif imc > 30 <= 40:
#    print(
#            'Seu IMC é: {:.1f} e você se encontra com obesidade.'.format(imc)
#    )
#elif imc > 40:
#    print(
#            'Seu IMC é: {:.1f} e você se encontra em obesidade mórbida.'.format(imc)
#    )

# Lógica de pagamento
#
#preco = float(input(
#                    'Qual é o valor normal do produto? '
#))
#
#print(
#                        """Métodos de pagamento possíveis:
#                        \033[0;33;1m1. Dinheiro\033[m
#                        \033[0;32;1m2. Cheque\033[m
#                        \033[0;35;1m3. À vista no cartão (Digite apenas cartão)\033[m
#                        \033[0;31;1m4. 2x no Cartão (Digite apenas o número de parcelas)\033[m
#                        \033[0;34;1m5. 3x ou mais no cartão (Digite apenas o número de parcelas, até 5x)\033[m"""
#)
#
#pagamento = str(input(
#                        'Qual é o método de pagamento? '
#)).strip().capitalize()
#
#if pagamento == "Dinheiro" or pagamento == "Cheque":
#    print(
#                """O método de pagamento escolhido foi: \033[0;33;1m{}\033[m
#                \033[0;34;1mO valor a ser pago será de: {:.2f}\033[m""".format(pagamento, preco - ((preco*10)/100))
#    )
#
#if pagamento == "Cartao":
#    print(
#                """O método de pagamento escolhido foi: \033[0;33;1mà vista no {}\033[m
#                 \033[0;34;1mO valor a ser pago será de {:.2f}\033[m""".format(pagamento, preco - ((preco*5)/100))
#    )
#
#if pagamento == "2x":
#    print(
#                """O método de pagamento escolhido foi: \033[0;33;1m{} no cartão\033[m
#                \033[0;34;1mO valor a ser pago será de: {:.2f}\033[m""".format(pagamento, preco)
#    )
#
#if pagamento == "3x" or pagamento == "4x" or pagamento == "5x":
#    print(
#                """O método de pagamento escolhido foi: \033[0;33;1m{} no cartão\033[m
#                \033[0;34;1mO valor a ser pago será de: {:.2f}\033[m""".format(pagamento, preco + ((preco*20)/100))
#    )
#    

# Jokenpô
import random

choice = str(input(
                        """Qual vai ser a sua jogada?
1. Pedra 
2. Papel
3. Tesoura
                        Digite aqui: """
)).strip().capitalize()

possib = [
            "Pedra", 
            "Papel", 
            "Tesoura"
        ]

computer = random.choice(possib)

if choice == "Pedra" and computer == "Pedra" or choice == "Tesoura" and computer == "Tesoura" or choice == "Papel" and computer == "Papel":
    print(
        "Eu escolhi {}, portanto empatamos!".format(computer)
        )

elif choice == "Pedra" and computer == "Tesoura" or choice == "Tesoura" and computer == "Papel" or choice == "Papel" and computer == "Pedra":
    print(
        "Eu escolhi {}, portanto você ganhou!".format(computer)
        )

elif choice == "Tesoura" and computer == "Pedra" or choice == "Papel" and computer == "Tesoura" or choice == "Pedra" and computer == "Papel":
  print(
   "Eu escolhi {}, portanto eu ganhei!".format(computer))