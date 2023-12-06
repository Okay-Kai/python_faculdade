# Este programa realiza cadastros de produtos para um hortifruti, e permite realizar uma busca pelos produtos após o cadastro. Digite 'Fim' para encerrar o programa
def cadastro(horti, nav):
    qnt = int(nav)                                      #<- Converte o valor de nav (recebido fora da função) em uma quantidade inteira, para que possa ser usada na linha abaixo
    for x in range(qnt):                                #<- Realiza a iteração com base na quantidade recebida
        produto = input() 
        preco = eval(input())                           #<- Recebe o preço em forma de string (input()) e o converte em valor (eval())
        produto_cadastrado = [produto, float(preco)]    #<- Armazena os valores recebidos em um objeto de lista, que permite armazenar mais de um tipo
        horti.append(produto_cadastrado)
        ''' Adiciona a lista que contém o produto e seu preço à uma lista principal que representa o estoque total do hortifruti,
            criando uma matriz onde os nomes dos produtos estarão sempre na coluna [0] e seus preços estarão sempre na coluna [1]
            facilitando a navegação pelos produtos cadastrados'''

def consulta_cad(horti, produto):
    '''Esta função realiza a consulta para sabermos se o produto informado já foi cadastrado no sistema'''
    lin = 1                                             #<- Significa 'linha', e é implementada ao início da função para ser iterada futuramente e permitir a navegação pela matriz
    cadastrado = False
    while lin <= len(horti) and cadastrado != True:
        ''' Iremos repetir enquanto nosso referencial 'lin' for menor que o total de linhas da matriz E enquanto não identificarmos
            um produto cadastrado, para assim termos certeza de que: A. Verificamos todas as posições da coluna [0]; B. Iremos parar assim que
            encontrarmos um produto semelhante cadastrado '''
        if produto == horti[-lin][0]:
            '''[-lin] faz com que a verificação das linhas da matriz seja feita debaixo para cima; Optei em fazer assim pois achei mais prático
            do que elaborar uma operação para um index que se inicia em 0'''
            cadastrado = True
            print(horti[-lin][1]) #<- imprime o valor do produto que já foi cadastrado
        else:
            lin += 1 #<- itera o index lin no caso de não encontrarmos nenhum produto semelhante, para que possamos ler a próxima linha da matriz na próxima execução do laço
    return(cadastrado) #<- retorna falso se nenhum produto semelhante foi encontrado, e verdadeiro se foi encontrado

def busca():
    busca_prod = ''                             #<- inicializa a variavel busca_prod
    while busca_prod.lower != 'fim':            #<- inicia o laço de repetição uma vez que condição sempre será satisfeita ao iniciar a função
        busca_prod = input()                    #<- solicita o produto a ser procurado na lista
        if busca_prod.lower() != 'fim':         #<- encerra a busca por produto caso o usuário digite 'fim'; lower() converte os elementos da string para lower case (letra minúscula)
            cad = consulta_cad(horti, busca_prod) #<- chama a função anterior e armazena o retorno booleano em uma variável local da função
            if cad == False:                    #<- cad é uma abreviação para cadastrado
                 print('Produto nao cadastrado')
            else:                               #<- if cad == True:
                 print('Produto ja cadastrado')
        else:                                   #<- if busca_prod.lower() == 'fim':
            break                               #<- encerra o if e retorna ao while, que não será executado uma vez que busca_prod == 'fim'

horti = []                                      #<- lista principal que será passada como argumento
nav = input()                                   #<- abreviação de navegador, receberá um valor string, que será convertido para valor numérico dentro das funções
if nav.lower() != 'fim':                        #<- permite o usuário encerrar antes de realizar o cadastro ao digitar 'fim'
    cadastro(horti, nav)
    busca()
    