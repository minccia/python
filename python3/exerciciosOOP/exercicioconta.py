from conta import Conta

primeira_conta = Conta('Paola', '001001001001', 0)

contas = [primeira_conta]

conta_numero = int(input('Qual conta deseja acessar? \n [0] Paola \nDigite aqui: '))

if conta_numero in range(2):
    conta_selecionada = contas[conta_numero]

while True:
    escolha = int(input(
                            """Oque deseja fazer?
                            [0] Alterar nome do correntista
                            [1] Depositar
                            [2] Sacar
                            Digite aqui: """))
    
    if escolha == 0:
        conta_selecionada.AlterarNome()

    if escolha == 1:
        conta_selecionada.Depositar()

    if escolha == 2:
        conta_selecionada.Sacar()
