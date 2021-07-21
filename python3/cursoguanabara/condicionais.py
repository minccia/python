#import random

#num = int(input('Escolha um número: '))
#ran = random.randint(0,5)
#print('O número que eu escolhi foi: {}'.format(ran))

#if num == ran:
    #print('Parabéns! Você acertou')

#else:
    #print('Sinto muito, você perdeu.')


#Ler velocidade de umm carro e multar

#vel = int(input('A que velocidade o seu carro estava, em Km/h? '))

#print('-------------------------- Realizando Cálculos --------------------------------------------------------------------')
#if vel >= 80:
    #multa = (vel-80)*7
    #print('Sinto muito, parece que você foi multado. O valor da sua multa é: R${:.2f}'.format(multa))

#else: 
    #print('Que bom, parece que você não será multado desta vez.')

# Números ímpares e pares

#num = int(input('Digite um número: ')) # Lê um número
#divi = num%2 # Resto da divisão

#if divi == 1:
    #print('Este número é ímpar ')

#else:
    #print('Este número é par')

# Preço de uma viagem

#dist = int(input('Qual é a distância da viagem em Km/h? '))

#if dist <= 200:
    #print('O valor da passagem de uma viagem de {} Kms é: R${:.2f}'.format(dist, dist*1/2))

#else:
   # print('O valor da passagem de uma viagem de {} Kms é: R${:.2f}'.format(dist, dist*9/20))

# Anos bissextos

#ano = int(input('Insira um ano: '))

#print('Esse ano é bissexto?')

#resto = ano%4

#if resto == 0:
    #print('O ano de {} é bissexto, logo possui 366 dias.'.format(ano))

#else:
    #print('O ano de {} não é bissexto, logo possui 365 dias como os demais anos.'.format(ano))

# Maior dos números
#
#num1 = int(input('Me dê um número: '))
#num2 = int(input('Me dê outro número: '))
#num3 = int(input('Me dê mais um número: '))
#
#if num1 > num2 > num3:
#    print('O número {} é o maior entre eles.'.format(num1))
#    print('O número {} é o menor entre eles.'.format(num3))
#
#elif num1 > num3 > num2:
#    print('O número {} é o maior entre eles.'.format(num1))
#    print('O número {} é o menor entre eles.'.format(num2))
#
#elif num2 > num1 > num3:
#    print('O número {} é o maior entre eles.'.format(num2))
#    print('O número {} é o menor entre eles.'.format(num3))
#
#elif num2 > num3 > num1:
#    #print('O número {} é o maior entre eles.'.format(num2))
#    #print('O número {} é o menor entre eles.'.format(num1))

#elif num3 > num1 > num2:
    #print('O número {} é o maior entre eles.'.format(num3))
    #print('O número {} é o menor entre eles.'.format(num2))

#else:
    #print('O número {} é o maior entre eles.'.format(num3))
    #print('O número {} é o menor entre eles.'.format(num1))

# Aumento de salário

#salario = float(input('Qual é o valor do seu salário? '))
#
#if salario > 1250:
#    print('O valor do seu aumento é de: R${:.3f}'.format((salario*10)/100))
#
#else: 
#    print('O valor do seu aumento é de: R${:.3f}'.format((salario*15)/100))

# Triângulo

r1 = int(input('Me dê o valor em centímetros de uma reta '))
r2 = int(input('Me dê o valor em centímetros de uma outra reta '))
r3 = int(input('Me dê o valor em centímetros de mais uma reta '))

print('\033[0;33;40mÉ possível formar um triângulo com estas três retas?\033[m ')

absolute = r2-r3 
soma = r2 + r3

print('\033[0;33;40m------------------------- E N V I A N D O  M E N T I R A S -----------------------------------\033[m')
if absolute < r1 < soma:
    print('Sim, é possível formar um triângulo com estas três retas')
else:
    print('Não é possível formar um triângulo com estas três retas')
