#def bhaskara(n):
#    coa = (float(input("Qual é o valor do coeficiente A?"))) # Coeficiente A
#    cob = (float(input("Qual é o valor do coeficiente B?"))) # Coeficiente B
#    coc = (float(input("Qual é o valor do coeficiente C?"))) # Coeficiente C
#    delta = ((cob**2)-4*coa*coc)**(1/2) #Delta/Discriminante
##    divisor = ((2*coa)) # Divisor de delta

#    if coa == 0: # A igual a zero resulta no fim do progama.
#        print("O coeficiente A deve ser maior do que zero.")
#    else:
#        raiz_positiva = (((-cob+delta)/divisor)) # Primeira raíz possível (positiva)
#        raiz_negativa = (((-cob-delta)/divisor)) # Segunda raíz possível (negativa)

#    print("\n***********************************************************************\n")
#    return raiz_positiva,raiz_negativa

#print(bhaskara(1))

coeficiente_a = int(input('Qual é o valor do coeficiente A? '))
coeficiente_b = int(input('Qual é o valor do coeficiente B? '))
coeficiente_c = int(input('Qual é o valor do coeficiente C? '))

def Bhaskara(coeficiente_a, coeficiente_b, coeficiente_c):
    # If coeficient A == 0 bhaskara can't be done, so program ends. 
    if coeficiente_a == 0: 
        print('O coeficiente A deve ser maior do que zero.')
        return

    # Whole formula
    raizes = [  ]
    delta = ((coeficiente_b ** 2) - 4 * coeficiente_a * coeficiente_c) ** (1/2)
    raiz_positiva = (-coeficiente_b + delta) / (coeficiente_a * 2)
    raiz_negativa = (-coeficiente_b - delta) / (coeficiente_a * 2)
    raizes.append(raiz_positiva)
    raizes.append(raiz_negativa)
    return raizes

print(Bhaskara(coeficiente_a, coeficiente_b, coeficiente_c))
