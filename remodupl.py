for i in range(int(input())):
    expressao = input()
    counter = 0
    possivel = False
    for i in range(len(expressao)):
        if expressao[i] == '(':
            counter += 1 
        elif expressao[i] == ')':
            if possivel == False:
                counter -= 1
                possivel = True
            elif counter == 1:
                break
        elif possivel == True:
            counter = 0
            possivel = False
    if possivel and counter == 1:
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')