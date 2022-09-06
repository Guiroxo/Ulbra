numero = input('Qual seu número de identificação? ')
salario = float(input('Qual o seu salário fixo? '))
carros = int(input('Quantos carros você vendeu esse mês? '))
valor = float(input('Qual o valor da sua comissão por carro vendido? '))
comissao = carros * valor
salarioFinal = salario + comissao
print(f'O vendedor {numero} receberá este mês um total de: {salarioFinal} reais')