#1PASSO DEFINIR A FINÇÃO DIMENSÃO DO OBJETO DE ONDE VAI ME RETORNAR O VOLUME E O VALOR ATRIBUIDO
def abertura():
    print('Bem vindo à Andre Minato express. . . RU - 2818401')

def dimensoes_objeto():
#TRY PARA O LAÇO RETORNAR PRO INICIO CASO RECEBA ALGUM FALSE

    try:
        altura = int(input('Digite a altura do    objeto:  '))
        largura = int(input('Digite a largura do objeto: '))
        comp = int(input('Digite o comprimento do objeto: '))

        volume = altura * largura * comp
        print('O volume do objeto é: {} cm³ '.format(volume))
#ESTABELECER AS CONDIÇÕES DE VOLUME E RETORNAR O UM VALOR ATRIBUIDO
        if volume < 1000:
            return 10
        elif 1000 <= volume < 10000:
            return 20
        elif 10000 <= volume < 30000:
            return 30
        elif 30000 <= volume < 100000:
            return 50
        else:
            print('O volume excede o permitido. . .\nDigite novamente. . .')
            return False
#USE EXCEPT IF VOLUME != NUM
    except ValueError:
        print('Você digitou um valor não numérico:\nDigite novamente um valor válido. . . ')
        return False
#A LÓGICA DA PRIMEIRA FUNÇÃO SE USA NO RESTO DO PROGRAMA

def peso_objeto():
    try:
        peso = int(input('Digite o peso do objeto: '))
        print('O peso do objeto é: {}Kg '.format(peso))

        if peso <= 0.1:
            return 1
        elif 0.1 < peso <= 1:
            return 1.5
        elif 1 < peso <= 10:
            return 2
        elif 10 < peso <= 30:
            return 3
        else:
            print('O peso excede o permitido.\nDigite novamente um valor válido. . . ')
            return False

    except ValueError:
        print('Você digitou um valor não numérico:\nDigite novamente um valor válido. . . ')
        return False


def rota_objeto():
    try:
        print('Selecione a rota desejada:\n')
        print('RS: RJ -> SP ')
        print('BS: BH -> SP ')
        print('RB: RJ -> BH ')
        rota = input('>>')

        if rota == 'RS':
            return 1
        elif rota == 'BS':
            return 1.2
        elif rota == 'RB':
            return 1.5
        else:
            print('Digite uma rota válida. . . ')
            return False
    except ValueError:
        print('Digite uma rota válida. . . ')
        return False

#VALOR TOTAL = * MULT DO RETORNO DAS 3 VARIAVEIS
def calculo_valor(dimensao, peso, rota):
    valor_total = dimensao * peso * rota
    print('Total a pagar: {}(R$):  (dimensões: {} * peso: {} * rota: {})'.format(valor_total, dimensao, peso, rota))
#chamar a função abertura para o cabeçalho
abertura()

#condição para o laço seguir caso função receba True
while True:
    volume = dimensoes_objeto()
    if volume:
        while True:
            peso = peso_objeto()
            if peso:
                while True:
                    rota = rota_objeto()
                    if rota:
                        calculo_valor(volume, peso, rota)
                        break
                break
        break
