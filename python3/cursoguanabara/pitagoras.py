cateto_adjacente = int(input('Qual é o valor do cateto adjacente? '))
cateto_oposto = int(input('Qual é o valor do cateto oposto? '))

def Pitagoras(cateto_adjacente, cateto_oposto):
    hipotenusa = ((cateto_adjacente**2) + (cateto_oposto**2))**(1/2)
    return hipotenusa

print(Pitagoras(cateto_adjacente, cateto_oposto))


