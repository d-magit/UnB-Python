# Nota = 10.00
class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque

def adicionar_alfabeto(deque, alfabeto):
    for i in alfabeto:
        deque.add_front(i)
    return None

def decifrar(deque, texto_cifrado, chave):
    texto_final = ''
    for i in texto_cifrado:
        letra = ''
        while letra != i:
            letra = deque.remove_rear()
            deque.add_front(letra)
        for j in range(chave+1): 
            letra = deque.remove_front()
            deque.add_rear(letra)
        texto_final += letra
    return texto_final
    
def selecionar_subconjunto_missoes():
    w = int(input())
    tempo_restante = w
    m = int(input())
    o = int(input())
    alfabeto = Deque()
    adicionar_alfabeto(alfabeto, input())
    chave = int(input())
    missoes = sorted([decifrar(alfabeto, input()[1:-1], chave).split(',') for i in range(int(input()))], key=lambda item: int(item[1]))
    linhamatriz = [0 for _ in range(w + 1)]
    matriz = [linhamatriz[:] for _ in range(len(missoes) + 1)]
    for i in range(len(missoes)):
        for j in range(w+1):
            if int(missoes[i][1]) > j:
                matriz[i+1][j] = matriz[i][j]
            else:
                usa = int(missoes[i][2]) + matriz[i][j - int(missoes[i][1])]
                naousa = matriz[i][j]
                matriz[i+1][j] = max(usa, naousa)
    valor = matriz[-1][-1]
    solucao = []
    for i in range(len(missoes)):
        atual = len(matriz) - 1 - i
        if matriz[atual][w] != matriz[atual-1][w]:
            solucao.append(missoes[atual-1])
            w -= int(missoes[atual-1][1])
    for i in solucao:
        tempo_restante -= int(i[1])
    if m == 1:
        if o == 0:
            solucao = sorted(solucao, key=lambda item: (item[0], int(item[1]), int(item[2]), item[3]))
        elif o == 1:
            solucao = sorted(solucao, key=lambda item: (int(item[1]), item[0], int(item[2]), item[3]))
        elif o == 2:
            solucao = sorted(solucao, key=lambda item: (int(item[2]), item[0], int(item[1]), item[3]))
        else:
            solucao = sorted(solucao, key=lambda item: (item[3], item[0], int(item[1]), int(item[2])))
        for i in solucao:
            print(', '.join(i))
    print(f'Tempo restante: {tempo_restante}')
    print(f'Valor: {valor}')
    return None