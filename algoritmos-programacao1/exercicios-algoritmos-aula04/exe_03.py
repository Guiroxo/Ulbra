minutos = int(input('Quanto tempo você levou de viagem? '))
horas = minutos / 60
velocidade = int(input('Qual foi a sua velocidade média? '))
distancia = (horas * velocidade)
gasolina = distancia / 12
print(f'A distância da viagem foi: {distancia} km, A quantidade em litros de combustível consumido foi: {gasolina} litros ')
