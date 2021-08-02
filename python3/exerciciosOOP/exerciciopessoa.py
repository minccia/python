from pessoa import Pessoa

paola = Pessoa('Paola', 17, 76, 1.84)

pessoas = [paola]
state = 'Menu'

while state == 'Menu':
    menu = int(input('Qual pessoa você deseja interagir? \n[0] Paola \nDigite aqui: '))

    if menu in range(2):
        pessoa_selecionada = pessoas[menu]

    escolha = int(input(
                            """Oque você deseja fazer?
                            [0] Envelhecer a Pessoa
                            [1] Engordar a Pessoa
                            [2] Emagrecer a Pessoa
                            [3] Fazer a Pessoa crescer
                            Digite aqui: """))
    
    if escolha == 0:
        pessoa_selecionada.envelhecer()
    
    if escolha == 1:
        pessoa_selecionada.engordar()
    
    if escolha == 2:
        pessoa_selecionada.emagrecer()
    
    if escolha == 3:
        pessoa_selecionada.crescer()
