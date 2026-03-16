dias=float(input("Informe a quantidade de dias"))
horas=float(input("informe a quantidade de horas"))
segundos=float(input("informe a quantidade de segundos"))
minutos=float(input("informe a quantidade de minutos"))

dia= dias * 24 * 3600
hora= horas * 3600
minuto= minutos*60
soma=dia+hora+minuto+segundos

print(f"a quantidade de segundos é",soma)
