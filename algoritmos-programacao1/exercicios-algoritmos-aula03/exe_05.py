print('Calculando o sálario que o funcionário tem a receber.')
nome = input('Nome do funcionário: ')
horas = float(input('Horas trabalhadas: '))
valor = float(input('Quanto ganha por hora trabalhada? '))
salario = horas * valor
print(f'{nome} seu sálario a receber é: {salario} reais')