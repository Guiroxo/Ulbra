numero1 = int(input('Escolha seu primeiro número: '))
numero2 = int(input('Escolha seu segundo número: '))
if numero1 > numero2:
  print(f'O número maior escolhido é {numero1} e a diferença pelo seu segundo número é {numero1 - numero2}')
else:
  print(f'O número maior escolhido é {numero2} e a diferença pelo seu primeiro número é {numero2 - numero1}')
