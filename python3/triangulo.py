class Triangulo:
    def __init__(self, ca=0, co=0, hipotenusa=0):
        self.ca = ca
        self.co = co
        self.hipotenusa = hipotenusa 

    def pegar_hipotenusa(self):
        self.hipotenusa = (self.ca ** 2) + (self.co ** 2) ** (1/2)
        return self.hipotenusa

    def pegar_perimetro(self):
        perimetro = self.ca + self.co + self.hipotenusa
        return perimetro
