print('Calculando a quantidade de latas de tintas necessárias para a pintura')
altura = float(input('Qual a altura do seu tanque? '))
raio = float(input('Qual o raio do seu tanque? '))
areaBase = 3.14 * (raio * raio)
areaLateral = 2 * 3.14 * raio * altura
areaTotal = areaBase + areaLateral
print(f'area da base: {areaBase}. area lateral {areaLateral}. area total {areaTotal}')
total = ((areaTotal / 3) / 5 ) * 150
print(f'Gasto total {total} reais')