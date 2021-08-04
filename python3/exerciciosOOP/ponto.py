class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def ImprimirPonto(self):
        print(f'Os valores do ponto são, respectivamente, ({self.x},{self.y})')
    
class Retangulo:
    def __init__(self, largura, altura):
        self.altura = altura
        self.largura = largura