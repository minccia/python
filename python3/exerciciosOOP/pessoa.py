class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.idade += 1
        print(f'A pessoa envelheceu mais um ano, e agora tem {self.idade} anos.')

        if self.idade < 21:
            self.altura += 0.05
            print(f'Pela pessoa ter menos de 21 anos, ela também cresceu 0,5 centímetros, e agora tem {self.altura:.2f} de altura.')

    def engordar(self):
        self.peso += 1
        print(f'A pessoa engordou 1kg, e agora possui {self.peso} kilos.')

    def emagrecer(self):
        self.peso -= 1
        print(f'A pessoa emagreceu 1kg, e agora possui {self.peso} kilos.')

    def crescer(self):
        self.altura += 0.05
        print(f'A pessoa cresceu 0,5 centíḿetros, e agora possui {self.altura:.2f} de altura.')