from time import sleep

vidas = 5
pontos = 0
mochila = []

print('*' * 55)
print('BEM VINDO AO MAIOR JOGO DE AVENTURA DE TODOS OS TEMPOS!')
print('*' * 55)
sleep(1)
print()
nome = str(input('Digite seu nome, aventureiro(a): '))
print()
print(f'Bem vindo(a), {nome}, a esse mundo de aventuras!')
print(f'Você tem {vidas} vidas e {pontos} pontos!')
print()
sleep(1)
print('Você foi encontrado(a) vagando à noite numa cidade deserta.')
print('Bem... Não tão deserta assim.')
print()
choice1 = (int(input('Você acabou de encontrar um esquilo.\n1) Pegar esquilo\n2) Deixar esquilo\nO que você faz? ')))
if choice1 == 2:
    print('Tadinho do bichinho, você não tem dó de deixa-lo sozinho nesse mundo cão?')
    print('*' * 10)
    print(f'Vidas: {vidas}')
    print(f'Pontos: {pontos}')
    print(f'Mochila: {mochila}')
    print('*' * 10)
elif choice1 == 1:
    print('Parabéns, você é o mais novo dono de um lindo esquilo selvagem e nada carinhoso.')
    mochila.append('Esquilo')
    pontos += 10
    print('*' * 10)
    print(f'Vidas: {vidas}')
    print(f'Pontos: {pontos}')
    print(f'Mochila: {mochila}')
    print('*' * 10)
    sleep(1)
    print()
    print('Você continua andando e percebe que tem alguém olhando para uma vitrine na loja do outro lado da rua.\nEscolha seu próximo passo cuidadosamente:')
    choice2 = int(input('1) Deixar o indivíduo cuidar de sua própria vida\n2) Tocar no ombro dele e puxar conversa\nO que você faz? '))
    if choice2 == 1:
        print('Ele corre atrás de você e te arranca um braço.')
        vidas -= 1
        pontos -= 5
        print('*' * 10)
        print(f'Vidas: {vidas}')
        print(f'Pontos: {pontos}')
        print(f'Mochila: {mochila}')
        print('*' * 10)
    elif choice2 == 2:
        print('Ele não tem uma cara muito amigável. Você se assusta e\ntaca seu esquilo nele. O esquilo mastiga seus olhos mas ele consegue\nmatar o esquilo antes de morrer.')
        pontos += 5
        mochila.remove('Esquilo')
        print('*' * 10)
        print(f'Vidas: {vidas}')
        print(f'Pontos: {pontos}')
        print(f'Mochila: {mochila}')
        print('*' * 10)
sleep(1)
print()
print('Agora você encontrou um quadro negro (que, na verdade, é branco), e uma caneta para escrever.\nPara continuar a história, deve resolver a equação.')
choice3 = int(input('Se 3 gatos matam 3 ratos em 3 minutos, quanto tempo levarão 100 gatos para matar 100 ratos?\n1) 1 minuto\n2) 3 minutos\n3) 30 minutos\n4) 100 minutos\nQual a sua escolha? '))
if choice3 != 2:
    print('Você perdeu')
else:
    print('Parabéns, sua lógia e matemática estão afiados! Por favor, prossiga...')
    pontos += 5
    mochila.append('Caneta')
    print('*' * 10)
    print(f'Vidas: {vidas}')
    print(f'Pontos: {pontos}')
    print(f'Mochila: {mochila}')
    print('*' * 10)
