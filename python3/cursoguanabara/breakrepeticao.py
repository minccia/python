#numero = contador = soma = 0

#while True:
#    numero = int(input('Digite um número: [999 para parar]'))
#    if numero == 999:
#        break
#    contador += 1
#    soma += numero

#print(f'O número de números digitados foi {contador} e a soma de todos eles é {soma}')

#numero = 0
#while True:
#    numero = int(input('Digite um número para ver a tabuada dele: '))
#    if numero < 0:
#        break
#    print(f"""Tabuada
#            {numero} x 2 = {numero*2}
#            {numero} x 3 = {numero*3}
#            {numero} x 4 = {numero*4}
#            {numero} x 5 = {numero*5}
#            {numero} x 6 = {numero*6}
#            {numero} x 7 = {numero*7}
#            {numero} x 8 = {numero*8}
#            {numero} x 9 = {numero*9}
#            {numero} x 10 = {numero*10}""")

#from random import randint, choice

#escolha_jogador = soma = vitorias = 0
#par_ou_impar_jogador = 'none' 
#opçoes = ['impar', 'par']

#while True:
    # Definição de par ou impar para cada um dos jogadores
#    par_ou_impar_computador = choice(opçoes)
#    print(f'O computador escolheu {par_ou_impar_computador}')

#    if par_ou_impar_computador == 'impar':
#        par_ou_impar_jogador = 'par'
#    else:
#        par_ou_impar_jogador = 'impar'
    
#    print(f'Logo, você é {par_ou_impar_jogador}')
#
#   print('*'*20)

    # Escolha dos números para efetuar a soma
#    escolha_jogador = int(input('Escolha um número: '))
#    escolha_computador = randint(0, 10)
    
    # Cálculo e definição de vencedor e perdedor
#    soma = escolha_jogador + escolha_computador
#    resto = soma % 2
#    print(f'A soma foi {soma}')
#
#    if par_ou_impar_jogador == 'impar' and resto > 0 or par_ou_impar_jogador == 'par' and resto == 0:   
#        print('Jogador venceu')
#        print("")
#        vitorias += 1
#
#    else:
#        print(f'Jogador perdeu, seu número de vitórias seguidas foi {vitorias}')
#        break

# Variáveis e listas para o loop while
idade = homens = maiores_que_18 = mulheres_menores_que_20 = 0

while True:
    # Lê a idade e o sexo da pessoa
    idade = int(input('Qual é a idade da pessoa? '))
    sexo = str(input('Qual é o sexo da pessoa? [Masculino/Feminino] ')).strip().capitalize()[0]
   
   # Contadores de pessoas maiores de 18 anos,
   # Número de maiores de homens e número de mulheres menos que 20 anos.
    if sexo not in 'MasculinoFeminino':
        print('Inválido, por favor tente novamente.')
        break

    if idade > 18:
        maiores_que_18 += 1

    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulheres_menores_que_20 += 1
    
    # Pergunta se o usuário deseja continuar cadastrando pessoas no sistema
    prosseguir = str(input('Você deseja continuar? [S/N] ')).strip().upper()[0]

    if prosseguir in 'S':
        print('Ok')

    else:
        break

# Mostra os resultados
print(f"""O número de pessoas que possui mais de 18 anos é: {maiores_que_18}
O número de homens é: {homens}
E o número de mulheres com menos de 20 anos é: {mulheres_menores_que_20}""")
