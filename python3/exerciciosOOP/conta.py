class Conta:
    def __init__(self, nome, numero, saldo=0):
        self.nome = nome 
        self.numero = numero
        self.saldo = saldo

    def AlterarNome(self):
        self.nome = str(input('Qual será o novo nome do correntista? \nDigite aqui:'))
    
    def Depositar(self):
        self.saldo += float(input('Quanto você deseja depositar? '))
        deposito = self.saldo
        if deposito > 500:
            print(f'Wow! Este é um valor bem alto, você ganhará pontos com o banco após a transação, seu saldo atual é {self.saldo}')
        self.saldo = deposito

    def Sacar(self):
        saque = float(input('Quanto você deseja sacar? \nDigite aqui: '))

        if saque > self.saldo:
            print(f'A conta não possui saldo suficiente para realizar o saque, por favor tente novamente.')
            return

        else:
            self.saldo -= saque
            print(f'Saque realizado com sucesso. Seu saldo atual é {self.saldo}')