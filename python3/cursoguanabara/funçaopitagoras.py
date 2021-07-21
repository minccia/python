# Função Pitágoras

def pitagoras(n):
    ca = (int(input("Qual o valor do cateto adjacente?")))**2
    co = (int(input("Qual o valor do cateto oposto?")))**2
    hip = (ca+co)**(1/2)
    return hip

print(pitagoras(0)) # O parâmetro dentro da função Pitágoras é o número de vezes que a fórmula irá se repetir
