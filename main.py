while True:
    try:
        print('Algoritmo de soma')
        a = int(input('Insira um valor: '))
        b = int(input('Insira outro valor: '))
        resultado = a + b
        print('O resultado é: '+str(resultado))
    except ValueError:
        print ('Dado invalido')
        continue
    else:
        break