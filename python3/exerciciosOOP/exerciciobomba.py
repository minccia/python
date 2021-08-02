from bomba import BombaCombustível

primeira_bomba = BombaCombustível('Etanol', 3, 0)
segunda_bomba = BombaCombustível('Gasosa', 6, 0)

bombas = [primeira_bomba, segunda_bomba]

state = 'Menu'
while state == 'Menu':
    bomba = int(input(
                            """Qual combustível você deseja utilizar para abastecer?
                            [0] Etanol
                            [1] Gasosa
                            Digite aqui: """
))
    
    if bomba in range(2):
        bomba_selecionada = bombas[bomba]

    state = 'Interacao'

    while state == 'Interacao':
        escolha = int(input(
                                """"Oque você deseja fazer?
                                [0] Abastecer por Valor
                                [1] Abastecer por Litro
                                [2] Alterar o valor do combustível
                                [3] Alterar combustível
                                [4] Alterar quantidade na bomba
                                Digite aqui: """
))

        if escolha == 0:
            bomba_selecionada.abastecerporValor()
        
        elif escolha == 1:
            bomba_selecionada.abastecerporLitro()

        elif escolha == 2:
            bomba_selecionada.alterarValor()
    
        elif escolha == 3:
            state = 'Menu'
        
        elif escolha == 4:
            bomba_selecionada.alterarQuantidadeBomba()
        
        else:
            print('Inválido. Por favor tente uma opção válida.')