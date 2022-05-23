#criar uma lista dos cadastros produtos
#definir função cadastrar, consultar, e remover produto


lista_produtos = []
#
#definir as funções
def cadastroProduto(cod):
    print('Sistema de cadastro de produtos. ')
    print(f'Código do produto: {cod} ')
    nome = input('NOME do produto: ')
    fabricante = input('FABRICANTE do produto : ')
    valor = float(input('VALOR do produto: '))
    dicionarioProduto = {'cod' : cod, 'nome':nome, 'fabricante':fabricante, 'valor':valor}
    lista_produtos.append(dicionarioProduto.copy())

#
#
def consultarProduto():
    while True:
        try:
            print('Sistema de consulta de produtos. ')
            opConsulta = int(input('1- CONSULTAR TODOS OS PRODUTOS.\n'
                                   '2- CONSULTAR POR CÓDIDO DO PRODUTO\n'
                                   '3- CONSULTAR POR FABRICANTE\n'
                                   '4- VOLTAR\n'
                                   '>>>  '))
            if opConsulta == 1:
                print('LISTA DE TODOS OS PRODUTOS ')
                for produto in lista_produtos: #
                    for key, value in produto.items():
                        print(f'{key} : {value} ')

            elif opConsulta == 2:
                print('CONSULTA POR CÓDIGO ')
                codigo = int(input('Digite o código desejado: '))
                for produto in lista_produtos:
                    if(produto['cod'] == codigo):
                        for key, value in produto.items():
                            print(f'{key} : {value} ')

            elif opConsulta == 3:
                print('CONSULTA POR FABRICANTE ')
                fab = input('Digite o fabricante desejado: ')
                for produto in lista_produtos:
                    if(produto['fabricante'] == fab):
                        for key, value in produto.items():
                            print(f'{key} : {value} ')

            elif opConsulta == 4:
                return
            else:
                print('Digite somente operações válidas. ')
        except ValueError:
            print('Essa operação não existe. . .')
            break

#
#
def alterarProduto():
    print('Alterações/Exclusões de produtos.')
    alter = int(input('Digite o código do produto a ser removido:'))
    for produto in lista_produtos:
        if(produto['cod'] == alter):
            lista_produtos.remove(produto)


#inicio do programa
print('SISTEMA DE CADASTRO E CONSULTA DE PRODUTOS ANDRE MINATO - RU=2818401.')

cod_produto = 0
while True:
    try:
        op = int(input('Escolha a operação desejada\n1 - CADASTRAR PRODUTOS\n2- CONSULTAR PRODUTOS\n3- ALTERAR PRODUTOS\n4- SAIR\n>>>  '))

        if op == 1:
            cod_produto = cod_produto + 1
            cadastroProduto(cod_produto)
        elif op == 2:
            consultarProduto()
        elif op == 3:
            alterarProduto()
        elif op == 4:
            print('SAINDO DO SISTEMA . . . ')
            break
        else:
            print('Digite somente operações válidas. ')
    except ValueError:
        print('Essa operação não existe. . .')





