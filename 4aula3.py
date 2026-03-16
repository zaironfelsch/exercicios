'''Escreva um programa que pergunte a distância que
um passageiro deseja percorrer em km. Calcule o preço
da passagem, cobrando R$ 0,50 por km para viagens de
até 200 km e R$ 0,45 para viagens mais longas'''

distancia=float(input("Coloque aqui a distancia que deseja percorrer"))

calculo1=distancia*0.50
calculo2=distancia*0.45

if distancia>200:
    print("o valor a pagar pela passagem é de", calculo2)

elif distancia<200:
    print("O valor total a pagar pela viagem é de", calculo1)
