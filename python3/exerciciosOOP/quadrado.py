class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self):
        self.lado = int(input('Qual valor deseja atribuir ao lado do quadrado?\nDigite aqui: '))
        print('Alteração concluída.')
    
    def verLado(self):
        print(f'O valor do lado é: {self.lado}')

    def calcularArea(self):
        print(f'A área do quadrado é igual a: {self.lado * self.lado} centímetros quadrados')