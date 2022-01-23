from random import randint
while True:
    try:
        quantos = int(input('Quantos CPFs gostaria de gerar? '))
    except:
        print('Caracter Inválido! Tente novamente.')
        continue
    lista = []
    for c in range(quantos):
        cpf = str(randint(100000000,999999999))
        novo_cpf = cpf
        reverso = 10
        total = 0
        for index in range(19):
            if index > 8:
                index -= 9
            total += int(novo_cpf[index]) * reverso
            reverso -= 1
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)
                if d > 9:
                    d = 0
                novo_cpf += str(d)
                total = 0
        lista.append(novo_cpf)
    print(lista)
    option = ' '
    while option not in 'SsNn':
        option = str(input("Quer continuar gerando Cpf's? [S/N]: "))
    if option in 'Nn':
        break

    print('OUTRO TESTE')
    