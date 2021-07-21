def bhaskara(n):
    coa = (float(input("Qual é o valor do coeficiente A?"))) # Coeficiente A
    cob = (float(input("Qual é o valor do coeficiente B?"))) # Coeficiente B
    coc = (float(input("Qual é o valor do coeficiente C?"))) # Coeficiente C
    delta = ((cob**2)-4*coa*coc)**(1/2) #Delta/Discriminante
    divisor = ((2*coa)) # Divisor de delta

    if coa == 0: # A igual a zero resulta no fim do progama.
        print("O coeficiente A deve ser maior do que zero.")
    else:
        raiz_positiva = (((-cob+delta)/divisor)) # Primeira raíz possível (positiva)
        raiz_negativa = (((-cob-delta)/divisor)) # Segunda raíz possível (negativa)

    print("\n***********************************************************************\n")
    return raiz_positiva,raiz_negativa

print(bhaskara(1))