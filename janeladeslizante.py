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

lista = Deck()
size = int(input())
for i in input().split():
    lista.add_rear(int(i))

k = int(input())
for i in range(size - k):
    print(str(max(lista.window(k))), end='  ')
    lista.add_rear(lista.remove_front())
print(str(max(lista.window(k))))