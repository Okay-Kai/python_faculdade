def consulta_cad(horti, produto):
    lin = 1
    cadastrado = False
    while lin <= len(horti) and cadastrado != True:
        if produto == horti[-lin][0]:
            cadastrado = True
        else:
            lin += 1
    return(cadastrado)

def busca():
    busca_prod = ''
    while busca_prod.lower != 'fim':
        busca_prod = input('Digite um produto: ')
        if busca_prod.lower() != 'fim':
            cad = consulta_cad(horti, busca_prod)
            if cad == False:
                 print('Produto não cadastrado')
            else:
                 print('Produto já cadastrado')
        else:
            break
    return(cad)
    
def cadastro(horti, nav):
    qnt = int(nav)
    for x in range(qnt):
        produto = input()
        preco = eval(input())
        produto_cadastrado = [produto, float(preco)]
        horti.append(produto_cadastrado)
    print(horti)

horti = []
nav = input()
if nav.lower() != 'fim':
    cadastro(horti, nav)
    busca()
    