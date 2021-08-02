
#"Classe para triângulos retângulos
#Atributos: Catetos
#métodos: pegar_perimetro
#         pegar_hipotenusa"

from triangulo import Triangulo

triangulo_retangulo = Triangulo()

triangulo_retangulo.ca = int(input('Qual é o cateto adjacente? '))
triangulo_retangulo.co = int(input('Qual é o cateto oposto? '))

state = 'menu'
while state == 'menu':
    resposta = int(input(('Oque você deseja fazer? \n[1]Pegar a hipotenusa \n[2]Pegar o perímetro \n[3]Sair ')))
    print('')

    if resposta == 1:
        print('A hipotenusa é: ', triangulo_retangulo.pegar_hipotenusa())
        print('')
        
    elif resposta == 2:
        print('O perímetro é: ', triangulo_retangulo.pegar_perimetro())
        print('')

    elif resposta == 3:
        print('Encerrando o programa...')
        state = 'saindo'
    
    else: 
        print('Valor inválido, por favor insira um aceito.')
        print('')
