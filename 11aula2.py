'''Escreva um programa que pergunte a quantidade de
km percorridos por um carro alugado pelo usuário, assim
como a quantidade de dias pelos quais o carro foi
alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por km rodado.'''
print()
km=float(input("coloque aqui a quantidade de kilometros rodados"))
print()
days=int(input("coloque aqui a quantiade de dias com o carro"))
print()
calculo_dia=days*60
calculo_km=km*0.15
total=calculo_dia+calculo_km
print(f"O total a pagar pelo uso do carro é de", total)
