def acresc_lista(nome):
    lista_nomes.append(nome)

lista_nomes = []
nome = input('Insira um nome, ou insira 0 para parar a edição:\n')
while nome != '0':
    acresc_lista(nome)
    nome = input('Insira um nome, ou insira 0 para parar a edição:\n')
    if nome == '0':
        print(lista_nomes)