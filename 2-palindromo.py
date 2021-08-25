#%%
class Deck:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)
    
    def add_rear(self, item):
        self.items.append(item)
      
    def remove_rear(self):
        return self.items.pop()
    
    def remove_front(self):
        return self.items.pop(0)

    def window(self, k):
        return self.items[0:k]

palavras = input().split()
for i in range(len(palavras)):
    palavra = Deck()
    substrings = []
    palindromos = set()
    for j in palavras[i]:
        palavra.add_rear(j)
    for j in range(len(palavras[i])):
        for n in range(len(palavras[i]) - j):
            substrings.append(palavra.window(j+1))
            palavra.add_rear(palavra.remove_front())
        for n in range(j):
            palavra.add_rear(palavra.remove_front())
    for j in substrings[::-1]:
        if j[::-1] == j and len(j) >= 3:
            j = ''.join(j)
            ntem = True
            for n in palindromos:
                if j in n:
                    ntem = False
            if ntem:
                palindromos.add(j)
    if len(palindromos) >= 2:
        print(palavras[i])