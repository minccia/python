from quadrado import Quadrado

quadrado = Quadrado(1)

while True:
    escolha = int(input('Oque deseja fazer? \n[0] Mudar o Lado\n[1] Ver lado \n[2] Calcular a área \nDigite aqui: '))

    if escolha == 0:
        print('')
        quadrado.mudarLado()
        print('')
    
    if escolha == 1:
        print('')
        quadrado.verLado()
        print('')

    if escolha == 2:
        print('')
        quadrado.calcularArea()
        print('')