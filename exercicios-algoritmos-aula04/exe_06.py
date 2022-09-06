numero1 = int(input('Escolha seu primeiro número: '))
numero2 = int(input('Escolha seu segundo número: '))
numero3 = int(input('Escolha seu terceiro número: '))
multiplicacao = numero1 * numero2 * numero3
soma = numero1 + numero2 + numero3
subtracao = numero1 - numero2 - numero3
total = multiplicacao + soma + subtracao
print(f'Os números escolhidos foram: {numero1}, {numero2} e {numero3}')
print(f'A multiplicação desses números é: {multiplicacao}')
print(f'A soma desses números é: {soma}')
print(f'A subtração desses números é: {subtracao}')
print(f'A soma dos resultados acima é {total}')