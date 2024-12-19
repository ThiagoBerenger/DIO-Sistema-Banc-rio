import textwrap

def menu():
    menu = """\n
    =============== Menu ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print('\n Depósito realizado.')
    else:
        print('\n A operação falhou. Valor Inválido.')
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    execedeu_saldo = valor > saldo
    execedeu_limite = valor > limite
    execedeu_saques = numero_saques >= limite_saques

    if execedeu_saldo:
        print('\n Operação falhou! Você não tem saldo suficiente.')
    if execedeu_limite:
        print('\n Operação falhou! O Valor Excedeu o limite.')
    if execedeu_saques:
        print('\n Operação Falhou! Você excedeu o número máximo de saques.')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n Saque realizado!')

    else:
        print('\n Operação falhou! valor informado inválido.')

    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print('n Extrato')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo:\t\tR$ {saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input('Informe o seu CPF')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Usuário já cadastrado')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('informe a data de nascimento: ')
    endereco = input('Informe o endereço: ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso!')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Conta criada')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n Usuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            '''
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite, 
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,               
            )
        
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print('Selecione novamente a operação desejada.')

            
main()