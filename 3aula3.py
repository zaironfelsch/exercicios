''' Escreva um programa que pergunte o salário do
funcionário e calcule o valor do aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%.
Para inferiores ou iguais, de 15%'''

salario=float(input("Coloque aqui o valor do seu salario"))

calculo1=salario*0.10+salario
calculo2=salario*0.15+salario

if salario>1250:
    print("O seu novo salario é o TOTAL de", calculo1)

else:
    print("O seu novo salario é o TOTAL de", calculo2)


