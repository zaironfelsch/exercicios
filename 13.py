'''Faça um programa que leia 2 notas de um aluno,
calcule a média e imprima aprovado ou reprovado (para
ser aprovado a média deve ser no mínimo 6'''

nota1=float(input("Coloque a primeira nota"))
nota2=float(input("Coloque a segunda nota"))

calculo= nota1+nota2/2

if calculo>6:
    print("VOCE PASSOU")

else:
    print("VOCE NAO PASSOU SEU VERME")