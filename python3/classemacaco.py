class Macaco:
    def __init(self, nome, bucho):
        self.nome = nome
        self.bucho = bucho

    def comer(self, comida_selecionada):
        self.bucho.append(comida_selecionada)
        
    def verBucho(self):
        print('O bucho do macaco possui atualmente: \n', self.bucho)
        return
    
    def digerir(self):
        self.bucho = []
