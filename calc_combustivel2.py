# Esta versão é igual a calculo_combustivel.py mas simplificada para aceitação na plataforma do AVA
def calc_combustivel(consumo, distancia):
    qnt_gasta = distancia/consumo
    print(qnt_gasta)

tempo_viagem = eval(input())
velocidade = eval(input())
consumo = eval(input())

distancia = tempo_viagem * velocidade
calc_combustivel(consumo, distancia)



