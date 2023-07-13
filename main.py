menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

LIMITE_POR_SAQUE = 500
LIMITE_SAQUE_DIARIO = 3
saldo = 0
numeros_saques = 0
extrato = ''


def converter_para_inteiro(numero: str) -> int | None:
    try:
        numero = int(numero)
    except:
        return None
    return numero


def pedir_numero_inteiro() -> str:
    numero = input('digite um numero inteiro: ')
    return numero


while True:

    opcao = input(menu)

    if opcao == 'd':
        print('Deposito')
        numero = pedir_numero_inteiro()
        inteiro_numero = converter_para_inteiro(numero)
        if not inteiro_numero:
            print('Numero digitado não e um inteiro')
            continue
        saldo += inteiro_numero
        extrato += f'Deposito: {inteiro_numero}\n'

    elif opcao == 's':
        print('Saque')
        numero = pedir_numero_inteiro()
        inteiro_numero = converter_para_inteiro(numero)
        if not inteiro_numero:
            print('Numero digitado não e um inteiro')
            continue
        if inteiro_numero > saldo:
            print('Você não tem dinheiro suficiente na conta')
            continue
        if inteiro_numero > LIMITE_POR_SAQUE:
            print('O limite de saque e 500')
            continue
        if numeros_saques >= LIMITE_SAQUE_DIARIO:
            print('Você chegou ao limite de saque por dia')
            continue
        saldo -= inteiro_numero
        extrato += f'Saque: {inteiro_numero}\n'
        numeros_saques += 1

    elif opcao == 'e':
        print('Extrato ')
        print(f'{extrato} Saldo Total:{saldo}')
    elif opcao == 'q':
        break

    else:
        print('Operação Invalida')

