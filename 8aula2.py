""""Faça um programa que solicite o preço de uma mercadoria e o percuntual de desconto. Exiba o valor do desconto e o novo valor a pagar"""
print()
preço=float(input("Coloque aqui o preço da mercadoria"))
desconto=float(input("Coloque aqui o seu desconto"))
calculo=desconto/100
porcentagem=calculo*100
novo_preço=preço-porcentagem
print("O valor do desconto é de", porcentagem,"o novo valor da mercadoria é de", novo_preço)

