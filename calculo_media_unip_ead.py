# Calculando a média :: Análise e Desenvolvimento de Sistemas (UNIP - EAD)
# Média = 7 x Prova + 2 x PIM + 1 x AVA / 10

print('Deve usar PONTO (.) em vez de VÍRGULA (,) ao informar os valores!')
print('Exemplo: 5.5 (certo) :: 5,5 (errado)\n')

ava = float(input('Digite a nota do AVA: '))
media = 0
pim = float(input('Digite a nota do PIM: '))
prova = float(input('Digite a nota da Prova: '))

prova *= 7
pim *= 2
media = (ava + prova + pim) / 10
exame = 6 - media

print(f'\nSua média foi de {media::.2f}!')
if media >= 6:
    print('Parabéns, você PASSOU!!!')
else:
    print(f'Você ficou de exame por {exame:.2f}.')
