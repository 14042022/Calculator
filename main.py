while True:
    #iejur51934
    try:
        print('Algoritmo de soma')
        a = int(input('Insira um valor: '))
        b = int(input('Insira outro valor: '))
        operacao = int(input('Que tipo de operação você quer?'
                             '\n [1]Positivo        [2]Negativo'
                             '\n [3]Multiplicação   [4]Divisão\n'))
        if operacao == 1:
            resultado = a + b
            print('O resultado é: ' + str(resultado))
        if operacao == 2:
            resultado2 = a - b
            print('O resultado é: '+str(resultado2))
        if operacao == 3:
            resultado3 = a * b
            print('O resultado é: '+str(resultado3))
        if operacao == 4:
            resultado4 = a / b
            print('O resultado é: '+str(resultado4))

    except ValueError:
        print ('Dado invalido')
        continue
    else:
        break