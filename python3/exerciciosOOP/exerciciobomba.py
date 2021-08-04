from bomba import BombaCombustível
from cliproject.menuelement import MenuElement

primeira_bomba = BombaCombustível('Etanol', 3, 0)
segunda_bomba = BombaCombustível('Gasosa', 6, 0)
bombas = [primeira_bomba, segunda_bomba]


bomba = int(input(('Que tipo de combustível você deseja utilizar para abastecer? \n[0] Etanol\n[1] Gasosa\n Digite aqui: ')))

if bomba in range(2):
    bomba_selecionada = bombas[bomba]
    

menu = MenuElement('Oque você deseja fazer?')

menu.add_choice('Abastecer por valor', bomba_selecionada.abastecerporValor)
menu.add_choice('Abastecer por litro', bomba_selecionada.abastecerporLitro)
menu.add_choice('Alterar o valor do combustível', bomba_selecionada.alterarValor)
menu.add_choice('Alterar a quantidade na bomba', bomba_selecionada.alterarQuantidadeBomba)

while True:
    menu.run()