from classemacaco import Macaco

macaco_marrom = Macaco()
macaco_albino = Macaco()

macaco_marrom.nome = str(input('Dê um nome ao macaco marrom: '))
macaco_albino.nome = str(input('Dê um nome ao macaco albino: '))

macaco_marrom.bucho = [  ]
macaco_albino.bucho = [  ]

state = 'Menu'

while state == 'Menu':
    selecionado = int(input(
        """Qual dos dois macacos você deseja interagir? 
    [1] Macaco Marrom
    [2] Macaco Albino 
    Digite aqui: """))

    if selecionado == 1 or selecionado == 2:
        state = 'Macaco'
    

    while state == 'Macaco':
        resposta = int(input(
        """Parabéns pela aquisição do seu macaco! Oque você deseja fazer?
        [1] Comer
        [2] Ver bucho
        [3] Digerir
        [4] Trocar de macaco
        [5] Sair do programa 
        Digite aqui: """))
    
        if resposta == 1 and selecionado == 1:
            
            indice_comida = int(input(f"""Oque deseja dar para o {macaco_marrom.nome} comer?
        [1] Banana
        [2] Sorvete
        [3] Quenga de coco
        [4] Outro Macaco (PERIGO!!!!!!!!) """))

            comidas = [ 
                    'banana',
                    'sorvete',
                    'quenga de coco',
                    'macaco'
                  ]
        
            comida_selecionada = comidas[indice_comida-1]
            macaco_marrom.comer(comida_selecionada)
            print(f'O senhor {macaco_marrom.nome} comeu {comida_selecionada}')

        if comida_selecionada == comidas[-1]:
            print('O MACACO COMEU OUTRO MACACO AAAAAAAAAAAAAAAAAAAAA')

                
        if resposta == 2 and selecionado == 1:
            print('')
            macaco_marrom.verBucho()
            print('')
        
        if resposta == 3 and selecionado == 1:
            macaco_marrom.digerir()
            print('O macaco digeriu tudo, e agora o bucho ficou vazio!', macaco_marrom.bucho)
            print('')
        
        if resposta == 1 and selecionado == 2:
            print('')
            macaco_albino.comer()
            print('')
        
        if resposta == 2 and selecionado == 2:
            print('')
            macaco_albino.verBucho()
            print('')
        
        if resposta == 3 and selecionado == 2:
            macaco_albino.digerir()
            print('O macaco digeriu tudo, e agora o bucho ficou vazio!', macaco_albino.bucho)
            print('')
        
        if resposta == 4:
            state = 'Menu'

        if resposta == 5:
            print('Encerrando o programa...')
            state = 'Saindo'
