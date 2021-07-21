# Tipo Int/Float/String
n1 = float(input('Digite um valor qualquer:'))
n2 = float(input('Digite outro valor qualquer:'))
s = n1+n2

print(f'A soma entre {n1} e {n2} vale: {s}')

# Boolean: Only receives True or False as an argument

n = input('Digite algo: ')

print(n.isupper())

# DESAFIO 1 - Identificar a classe de input() e obter o máximo de informações possíveis sobre o valor digitado

n = input('Digite algo do teclado: ')

print('O seu tipo primitivo é:', type(n)) # Qual seu tipo primitivo
print('É numérico? ', n.isnumeric())
print('Só tem espaços? ', n.isspace())
print('É alphanumérico? ', n.isalnum())
print('Só tem letras maísculas? ', n.isupper())
print('Só tem letras minúsculas? ', n.islower())
print('É um título? ', n.istitle())
print('É um ASCII? ', n.isascii())
print('É um dígito? ', n.isdigit())
print('É printável? ', n.isprintable())
print('É um identificador? ', n.isidentifier())









