class Retangulo:
    def __init(self, base, altura, area=0):
        self.base = base
        self.altura = altura
        self.area = self.base * self.altura

    def MudarLados(self):
        self.base = int(input('Qual será o valor da base? '))
        self.altura = int(input('Qual será o valor da altura? '))
        print('Mudança concluída!')
        print('')
    
    def Area(self):
        area = self.base * self.altura
        print(f'A área do retângulo é igual a: {area} metros quadrados')
        print('')

    def Perimetro(self):
        perimetro = (2 * self.altura) + (2 * self.base)
        print(f'O perímetro do retângulo é igual a: {perimetro} metros quadrados')
        print('')

    def NumeroDePisos(self):
        base_do_piso = float(input('Qual é a medida da base do piso? '))
        altura_do_piso = float(input('Qual é a medida da altura do piso? '))
        area_do_piso = base_do_piso * altura_do_piso
        area = self.base * self.altura
        pisos = area / area_do_piso
        print(f"""O número de pisos necessários para o local é de {pisos + 1 + (pisos * 10)/100:.0f}""")
        print('')
    
    def Rodape(self):
        rodape_altura = self.altura * 0,15
        roda_base = self.base * 0,15
        quantidade_de_rodape = (rodape_altura + roda_base) * 2
        print(f'A quantidade necessária de rodapé será de: {quantidade_de_rodape}')

