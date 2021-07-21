#n1 = float(input('Digite um número :'))
#n2 = float(input('Digite outro número :'))

#s = n1+n2
#m = n1*n2
#d = n1/n2
#p = n1**n2
#di = n1//n2
#re = n1%n2

#print('A soma é {}, a multiplicação é {}, a divisão é {:.2f} e a potência é {:.2f}'.format(s, m, d, p), end=' ')
#print('A divisão inteira é {} e o resto da divisão é {}'.format(di, re))

# Desafio 1
#n1 = float(input('Insira um número para descobrir o seu antecessor e o seu sucessor: '))
#ant = n1-1
#suc = n1+1

#print('O número escolhido foi {}, o seu antecessor é {} e o seu sucessor é {}.'.format(n1, ant, suc))

# Desafio 2

# n = float(input('Insira um número :'))
# do = n*2 # Dobro do número N
# tri = n*3 # Triplo do número N
# squ = n**(1/2)

# print('O número escolhido foi {}. O dobro desse número é {}, o triplo é {}, e a raíz quadrada é {:.2f}.'.format(n, do, tri, squ))

# Desafio 3

#n1 = float(input('Qual é a sua primeira nota? :'))
#n2 = float(input('Qual é a sua segunda nota? :'))
#m = (n1+n2)/2

#print('A sua primeira nota é {}, a sua segunda nota é {}, e a média aritmética entre elas é {:.2f}.'.format(n1, n2, m))

#va = float(input('Qual é o valor em metros que você deseja converter?:'))
#cm = va*10*10
#mm = va*10*10*10

# print(float(input('O valor em metros é: {}, o valor em centímetros é: {}, e o valor em milímetros é: {}.'.format(va, cm, mm))))

# Faça um progama que leia um número inteiro e mostre a tabuada dele

#n = int(input('Insira um número inteiro para ver a tabuada dele: '))

#def tabuada(n):
   # n1 = n*2
   # n2 = n*3
   # n3 = n*4
   # n4 = n*5
   # n5 = n*6
   # n6 = n*7
   # n7 = n*8
   # n8 = n*9
   # n9 = n*10
   # tabu = ' Seu número x2 é: {} \n Seu número x3 é: {} \n Seu número x4 é: {} \n Seu número x5 é: {} \n Seu número x6 é: {} \n Seu número x7 é: {} \n Seu número x8 é: {} \n Seu número x9 é: {} \n Seu número x10 é: {}'.format(n1, n2, n3, n4, n5, n6, n7, n8, n9)
   # return tabu
    
#print(tabuada(n))

# Desafio 4

#cash = float(input('Quanto de dinheiro você tem na carteira?'))
#dol = cash/3.27

#print('A quantidade de dólares que você pode comprar com esse valor é: ${:.2f}'.format(dol))

#altura = float(input('Quantos metros de altura tem a sua parede? '))
#largura = float(input('Quantos metros de largura tem a sua parede? '))
#area = altura*largura
#tinta = area/2

#print('================================================================================================')

#print('A área da sua parede possui {} metros quadrados, portanto você vai precisar de no mínimo {} litros de tinta para pintar-la completamente.'.format(area, tinta))

# Desafio 5

#pri = float(input('Qual é o preço do produto? '))
#porc = (pri*5)/100
#desc = pri - porc

#print('********************************************************************************************')

#print('O valor deste produto, com 5% de desconto, fica no valor de: {:.2f}'.format(desc))

# Desafio 6

sal = float(input('Qual é o valor atual do seu salário? '))
porc = (sal*15)/100
aum = sal + porc

print('***********************************************************************************************')

print('O valor do seu salário, com um aumento de 15%, fica no valor de: {:.2f}'.format(aum))