salario= float(input("informe seu salario"))
porcentagem= float(input("informe a porcentagem do seu aumento"))

calculo=salario*porcentagem/100
valor_do_aumento=calculo
valor_do_novo_salario= salario+calculo
print("O valor do seu novo salario é o total de ",valor_do_novo_salario, "e o valor do seu novo aumento fica no total de ",valor_do_aumento)

