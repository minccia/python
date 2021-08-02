from bola import Bola

bola_de_gude = Bola("Nenhuma", 5, "Vidro")
bola_de_ferro = Bola("Nenhuma", 15, "Ferro")

bolas = [bola_de_gude, bola_de_ferro]
bola_escolhida = bolas[0]

def interagir():
    print('')
    escolha = int(input('Oque deseja fazer? \n[0] Trocar Cor da Bola \n[1] Ver cor da Bola \nDigite aqui: '))
    print('')

    if escolha == 0:
        bola_escolhida.trocaCor()
        print('')

    elif escolha == 1:
        bola_escolhida.mostraCor()
        print('')
    

state = 'Menu'

while state == 'Menu':
    bola_numero = str(input('Com qual bola deseja interagir? \n[0] Bola de Gude\n[1] Bola de Ferro \nDigite aqui: '))

    if bola_numero in range(2):
        bola_escolhida = bolas[bola_numero]

    interagir()





