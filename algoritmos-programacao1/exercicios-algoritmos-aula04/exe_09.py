print('Preço do computador')
valor = float(input('Qual o preço de fábrica do computador? '))
revenda = float(valor * 0.45)
print(f'O valor adicional de revenda é {revenda} reais ')
imposto = float(valor * 0.28)
print(f'O valor do imposto é {imposto} reais ')
final = valor + revenda + imposto 
print(f'Valor final do computador é {final}')