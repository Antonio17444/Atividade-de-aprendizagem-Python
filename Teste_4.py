#Scripts: 

#introdução do programa | Dados do Usuario

print('==============================================================================')
while True:
    print(' ')
    print('Olá Usuário, é hora de controlar as suas finanças com o Finance!!')
    print(' ')
    print('Vamos começar com seu cadastro, favor preencher o formulário abaixo: ')
    print(' ')
    print(' ')
    user_name = str(input('Informe seu nome de Usuário: '))
    user_idade = int(input('Certo... {} qual é sua idade? '.format(user_name)))
    email = (input('Informe seu E-mail: '))
    print(' ')
    print('Certo... ')
    print(' ')
    print('Agora vamos fazer o cadastro da sua senha ')
    print(' ')
    user_senha = input('Defina sua senha: ')
    print(' ')
    print('==============================================================================')
    print(' ')
    print('Agora vamos confirmar suas informações')
    print(' ')
    while True:
        print(f'Nome: {user_name}')
        print(f'Idade: {user_idade}')
        print(f'Senha: {user_senha}')
        print(f'Email: {email}')
        print(' ')
        resposta = input("As informações estão corretas? (sim/não): ").strip().lower()
        
        if resposta == 'sim':
            print(' ')
            print("Informações confirmadas! Continuando o programa...")
            break
        elif resposta == 'não':
            print("Vamos reiniciar a entrada de informações.\n")
            break
        else:
            print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
    
    if resposta == 'sim':
        break
print('==============================================================================')
print(' ')
print('Com base no seu sálario mensal, vamos realizar um balanço das suas despezas e fechar o mês no positivo!')
print(' ')
user_salario = float(input('Informe o seu ganho mensal (Salário/entre outros): '))
print(' ')
print((f'Como você faz a distribuição do seu sálario de {user_salario}?'))
print('Preencha a tabela de distribuição: ')

#Preenchimento das variaveis pelo usuario

alimento = float(input('Quanto você gasta com alimentação por mês? R$ '))
medicamento = float(input('Quanto você gasta com medicação por mês? R$ '))
saude = float(input('Quanto você gasta com sua saúde por mês? R$ R$ '))
lazer = float(input('Quanto você gasta com seu lazer por mês? R$ '))
transporte = float(input('Quanto você gasta em transporte por mês? R$ '))
habitacao = float(input('Quanto você gasta em aluguel/habitação por mês? R$ '))
outros = float(input('Quanto em gastos gerais? R$ '))
print(' ')
if user_salario > (alimento+medicamento+saude+lazer+transporte+habitacao+outros):
  print('\033[32mÓtimo, seus gastos estão abaixo do seu ganho!.\033[0m')
else:
   print('\033[31mO seu salário está abaixo dos seus gastos!\033[0m')
print(' ')

#Criação das variaveis com espaços

user_alimento = str(alimento).ljust(10)
user_medicamento = str(medicamento).ljust(10)
user_saude = str(saude).ljust(10)
user_lazer = str(lazer).ljust(10)
user_transporte = str(transporte).ljust(10)
user_habitacao = str(habitacao).ljust(10)
user_outros = str(outros).ljust(10)

#Tabela de gastos do usúario

print('\033[33m|  Categoria   |   Gastos   |\033[0m')
print('\033[33m|--------------|------------|\033[0m') 
print('\033[33m|  Alimentação | {} |\033[0m'.format(user_alimento))
print('\033[33m|   Medicação  | {} |\033[0m'.format(user_medicamento))
print('\033[33m|     Saúde    | {} |\033[0m'.format(user_saude))
print('\033[33m|     Lazer    | {} |\033[0m'.format(user_lazer))
print('\033[33m|  Transporte  | {} |\033[0m'.format(user_transporte))
print('\033[33m|   Habitação  | {} |\033[0m'.format(user_habitacao))
print('\033[33m|    Outros    | {} |\033[0m'.format(user_outros))
print(' ')

print('==============================================================================')
