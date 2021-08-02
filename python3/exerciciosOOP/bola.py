class Bola:
    def __init__(self, cor, circunferencia, material, indice_cor=0):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
        self.indice_cor = indice_cor

    def trocaCor(self):
        cores = [ 'Azul', 'Verde', 'Vermelho', 'Preto', 'Branco', 'Rosa', 'Transparente', 'Laranja' ]
        print(f'As cores disponíveis são: \n{cores}')
        print('')

        if self.indice_cor == len(cores):
            self.indice_cor = 0

        self.cor = cores[self.indice_cor]
        self.indice_cor += 1

        print(f'A cor da bola agora é {self.cor}.' )
        return 
        
    def mostraCor(self):
        print(f'A cor da bola, atualmente, é: {self.cor}.' )
        return

