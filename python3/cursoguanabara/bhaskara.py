  # Progama para resolver a fórmula de Bhaskara e encontrar as raízes possíveis

coa = (int(input("Qual é o valor do coeficiente A?"))) # Coeficiente A
cob = (int(input("Qual é o valor do coeficiente B?"))) # Coeficiente B
coc = (int(input("Qual é o valor do coeficiente C?"))) # Coeficiente C

delta = ((cob**2)-4*coa*coc)**(1/2) # Delta/Discriminante
divisor = int((2*coa)) # Divisor
raiz_positiva = (((-cob+delta)/divisor)) # Primeira raíz possível
raiz_negativa = (((-cob-delta)/divisor)) # Segunda raíz possível

print("As raízes possíveis para os coeficientes dados são:")
print(raiz_positiva,raiz_negativa)