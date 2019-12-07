# Calculando a média em Python :: Análise e Desenvolvimento de Sistemas (UNIP - EAD)
# Média = (7 x Prova) + (2 x PIM) + (1 x AVA) / 10

# Autor :: Daniel Buck
# Dezembro de 2019

# Importando o "timer" pra dar um suspense extra ao aguardar pela média
from time import sleep

# Declarando "opção" para o menu e "média" para calcular posteriormente
opt = 0
media = 0

# Instruções de uso
print('Deve usar PONTO (.) em vez de VÍRGULA (,) ao informar os valores!')
print('Exemplo: 5.5 (certo) :: 5,5 (errado)\n')

# Suspense
sleep(1)

# Início do loop 'while'
while opt != 2:

    # Menu
    print("\n[1] Calcular média\n[2] Encerrar programa")
    opt = int(input(">>> "))

    # Usando a opção de calcular média do menu
    if opt == 1:

        # Inserção das notas para cálculo
        materia = str(input('\nDigite o nome da matéria: '))
        ava = float(input('Digite a nota do AVA: '))
        prova = float(input('Digite a nota da Prova: '))
        pim = float(input('Digite a nota do PIM: '))

        # Calculando notas e médias
        prova *= 7
        pim *= 2
        media = (ava + prova + pim) / 10
        exame = 6 - media

        sleep(1)

        # Apresetação dos resultados
        print(f'\nSua média em {materia} foi de {media:.2f}!')

        sleep(1)

        if media >= 6:
            print('Parabéns, você PASSOU!!!')
        else:
            print(f'Você ficou de exame por {exame:.2f}.')

    # Usando a opção de encerrar o sistema do menu
    elif opt == 2:
        print("\nObrigado e volte sempre!")

    # Mostrando uma mensagem de erro ao inserir uma opção inválida
    else:
        print("\nOpção inválida, tente novamente.")
