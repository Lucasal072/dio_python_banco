from sys import exit

menu_usuario_str = '''
[c] Criar usuario
[e] Entrar usuario
=> '''

menu_conta_str = '''
[l] Listar contas
[c] Criar conta
[e] Entrar conta
=> '''

menu_opcoes_str = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> '''

LIMITE_POR_SAQUE = 500
LIMITE_SAQUE_DIARIO = 3
index_account = 1

database = {}


def mostrar_extrato(conta: dict):
    print(f'{conta["extrato"]}{conta["saldo"]}')


def criar_usuario():
    cpf = input('digite o seu cpf: ')
    cpf_formatado = cpf.replace('.','').replace('-','')
    if database.get(cpf_formatado):
        print('cpf ja esta cadastrado')
        return
    nome = input('digite o seu nome: ')
    data_de_nascimento = input('data de nascimento: ')
    logradouro = input('logradouro: ')
    numero_casa = input('numero da casa: ')
    bairro = input('bairro: ')
    cidade = input('cidade: ')
    estado = input('UF estado: ')
    endereco = f'{logradouro} - {numero_casa} - {bairro} - {cidade} - {estado}'
    database[cpf_formatado] = {
        'nome': nome,
        'data_de_nascimento': data_de_nascimento,
        'endereco': endereco,
        'contas': {}
    }


def criar_conta(usuario: dict):
    global index_account 
    usuario['contas'][f'000{index_account}'] = {
        'saldo': 0,
        'limite_saque': 0,
        'extrato': ''
    }
    index_account += 1


def listar_contas(usuario: dict):
    for numero_conta in usuario['contas'].keys():
        print(numero_conta)


def converter_para_inteiro(numero: str) -> int | None:
    try:
        numero = int(numero)
    except:
        return None
    return numero


def pedir_numero_inteiro() -> str:
    numero = input('digite um numero inteiro: ')
    return numero


def deposito(valor: int, conta: dict, /):
    conta['saldo'] += valor
    conta['extrato'] += f'Deposito: {valor}\n'


def saque(*, valor: int, conta: dict):
    if valor > conta['saldo']:
        print('Você não tem dinheiro suficiente na conta')
        return
    if valor > LIMITE_POR_SAQUE:
        print('O limite de saque e 500')
        return
    if conta['numero_saque'] >= LIMITE_SAQUE_DIARIO:
        print('Você chegou ao limite de saque por dia')
        return
    conta['saldo'] -= valor
    conta['extrato'] += f'Saque: {valor}\n'
    conta['numero_saque'] += 1


def menu_usuario():
    while True:
        opcao_usuario = input(menu_usuario_str).lower()
        if opcao_usuario == 'c':
            criar_usuario()
        elif opcao_usuario == 'e':
            cpf = input('digite o cpf ')
            cpf_formatado = cpf.replace('.', '').replace('-', '')
            usuario = database.get(cpf_formatado)
            if not usuario:
                print('usuario não encontrado')
                continue
            menu_conta(database[cpf_formatado])
        elif opcao_usuario == 'q':
            exit()
        else:
            print('Operação Invalida')


def menu_conta(usuario: dict):
    while True:
        opcao_conta = input(menu_conta_str).lower()
        if opcao_conta == 'l':
            listar_contas(usuario)
        elif opcao_conta == 'c':
            criar_conta(usuario)
        elif opcao_conta == 'e':
            numero_conta = input('numero da conta')
            conta = usuario['contas'].get(numero_conta)
            if not conta:
                continue
            menu_opcoes(usuario['contas'][numero_conta])
        elif opcao_conta == 'q':
            exit()
        else:
            print('Operação Invalida')


def menu_opcoes(conta: dict):
    while True:
        opcao = input(menu_opcoes_str).lower()

        if opcao == 'd':
            print('Deposito')
            numero = pedir_numero_inteiro()
            numero_inteiro = converter_para_inteiro(numero)
            if not numero_inteiro:
                print('Numero digitado não e um inteiro')
                continue
            deposito(numero_inteiro, conta)

        elif opcao == 's':
            print('Saque')
            numero = pedir_numero_inteiro()
            numero_inteiro = converter_para_inteiro(numero)
            if not numero_inteiro:
                print('Numero digitado não e um inteiro')
                continue
            saque(valor=numero_inteiro, conta=conta)

        elif opcao == 'e':
            mostrar_extrato(conta)

        elif opcao == 'q':
            exit()

        else:
            print('Operação Invalida')

menu_usuario()