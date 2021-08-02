class BombaCombustível:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel, quantiaBomba=200):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
        self.quantiaBomba = quantiaBomba

    def abastecerporValor(self):
        valor = float(input('Qual valor será abastecido? '))
        print(f'A quantidade de litros que foi abastecido é: {valor/self.valorLitro:.2f}')
        self.quantiaBomba -= valor / self.valorLitro
        
    def abastecerporLitro(self):
        self.quantidadeCombustivel = int(input('Quantos litros você quer abastecer? '))
        print(f'O valor a ser pago será de: {self.quantidadeCombustivel*self.valorLitro:.2f}')
        self.quantiaBomba -= self.quantidadeCombustivel

    def alterarValor(self):
        self.valorLitro = float(input(f'Qual será o valor do litro de {self.tipoCombustivel} agora? '))
        print('Alteração feita')

    def alterarQuantidadeBomba(self):
        encher_bomba = int(input(f'A bomba possui {self.quantiaBomba} litros. Quantos litros deseja encher-la? '))
        self.quantiaBomba += encher_bomba
        print(f'A bomba foi enchida e agora possui {self.quantiaBomba} litros')