# Lê um número real qualquer e printa sua parte inteira

#from math import ceil, floor # Importar a biblioteca "Math"

#num = float(input('Digite um número real qualquer: ')) # Lê um número real qualquer pelo teclado
#print('A parte inteira do número {} é: {:.2f} '.format(num, floor(num)))

# Lê o cateto oposto e o cateto adjacente e mostra a hipotenusa

#from math import ceil # Importa "Ceil" da biblioteca "Math"
#ca = int(input('Qual é o valor do cateto adjacente?'))**2 # Lê o valor do cateto adjacente
#co = int(input('Qual é o valor do cateto oposto?'))**2 # Lê o valor do cateto oposto
#hip = (ca+co)**(1/2)

#print('O comprimento da hipotenusa é: {:.2f}'.format(ceil(hip)))

# Lê um ângulo qualquer e mostra os seus valores de seno, coseno e tangente

#from math import sin, cos, tan, degrees

#an = int((input('Digite um ângulo qualquer em radianos: ')))
#graus = degrees(an)
#print('Para o ângulo {:1f}, seus valores de seno, cosseno e tangente são, respectivamente, {:.2f}, {:.2f} e {:.2f}'.format(an, sin(graus), cos(graus), tan(graus)))

# Sortear uma ordem de alunos para apresentar trabalhos
#import random

#a1 = input('Qual é o nome do primeiro aluno?: ')
#a2 = input('Qual é o nome do segundo aluno?: ')
#a3 = input('Qual é o nome do terceiro aluno?: ')
#a4 = input('Qual é o nome do quarto aluno?: ') # Lê o nome dos alunos

#al = [a1, a2, a3, a4]
#ordem = random.sample(al, k=4)

#print('A ordem de apresentação dos alunos será: \n {}'.format(ordem))

# MP3 Player

import playsound

playsound('$HOME/dulis/meusscripts/cursoguanabara/faceshopping.mp3')