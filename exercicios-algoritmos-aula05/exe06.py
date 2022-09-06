from math import sqrt

numero1 = int(input('Escolha um número: '))
numero2 = int(input('Escolha mais um número: '))
numero3 = int(input('Escolha seu último número: '))
if numero1 > 0:
  print(sqrt(numero1))
else:
  print(numero1 * numero1)

if numero2 > 10 and numero2 < 100:
  print('Número está entre 10 e 100 (Intervalo permitido)')
else:
  print('Número inválido')

if numero3 < numero2:
  print(numero2 - numero3)
else:
  print(numero3 + numero2)