#frase = 'Curso em vídeo python'

#print((frase.find('Android')))
#len()
#frase.count
# 'Curso' in frase
# frase.split()
# '-'join.(frase)

# frase.replace('Python', 'Android')
#print(frase.upper())
# frase.lower
# frase.capitalize
# frase.title

#frase = '   Aprenda Python  '

#frase.strip() strip both sides
#frase.rstrip() right strip
#frase.lstrip() left strip

#print(frase.lower().replace('python', 'Miyamola'))

# Leitura nome completo

# Variável recebe um nome qualquer pelo teclado
#nome = str(input('Qual é o seu nome completo? ')).strip()

#print('*********************************************************************************************')

# Letras maiúsculas
#print('O seu nome com todas as letras maiúsculas é: {}'.format(nome.upper()))

#print('*********************************************************************************************')

# Letras minúsculas
#print('O seu nome com todas as letras minúsculas é: {}'.format(nome.lower()))

# Total de letras do nome

#print('O total de letras do seu nome é: {}'.format(len(nome) - nome.count(' ')))

# Quantas letras tem o primeiro nome
#num = nome.split()

#print('O total de letras do seu primeiro nome é: {}'.format((len(num[0]))))

 #Ler nome de cidade e dizer se começa com SANTO

#nome = str(input('Digite o nome de uma cidade: ')).strip()

#print('Essa cidade tem "Santo" no começo do nome?')

#tem = nome.capitalize().split()

#print('Santo' in tem)

# Ler nome de uma pessoa e dizer se tem silva no nome

#nome = str(input('Digite um nome: ')).title().strip()
#print('Essa pessoa tem "Silva" no nome?')

#print('Silva' in nome)

# Contar letra A

#frase = str(input('Digite uma frase: ')).upper().strip() # Recebe frase

#letra = frase.count('A') # Quantas letras A ela tem?
#print('Essa frase possui {} letras "A"'.format(letra))

#print('A letra A aparece a primeira vez na posição: {}'.format(frase.find('A')+1))
#print('A letra A apareceu a última vez na posição: {}'.format(frase.rfind('A')+1))

# Análise do nome

#nome = str(input('Qual é o seu nome? ')).title().strip().split()

#print('O seu primeiro nome é: {}'.format(nome[0]))
#print('O seu último nome é: {}'.format(nome[len(nome)-1]))
