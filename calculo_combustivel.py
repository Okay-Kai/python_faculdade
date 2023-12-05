def calc_combustivel(consumo, distancia):
    consumido = distancia/consumo
    print('A quantidade de combustível consumido durante a viagem foi:', round(consumido, 2), 'litros') # round(x, qnt_decimais): define quantas casas decimais serão mostradas além de arredondar o valor

tempo_viagem = eval(input('Informe o tempo de viagem em horas:\n'))
velocidade = eval(input('Informe a velocidade média do automóvel em Km/h:\n'))
consumo = eval(input('Informe o consumo médio do automóvel em Km/L:\n'))

distancia = tempo_viagem * velocidade
print('A distância percorrida foi', distancia, 'Km')
calc_combustivel(consumo, distancia)



