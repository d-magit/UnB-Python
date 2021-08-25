class Dynlist:
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
      
    def remove_pos(self, pos):
       return self.items.pop(pos-1)

    def subs(self, item1, item2):
        pos = self.items.index(item1)
        self.items.pop(pos)
        self.items.insert(pos, item2)

    def size(self):
        return len(self.items)

Lista = Dynlist()
entrada = [[]]
while entrada[0] != 'X':
    entrada = input().split()
    if entrada[0] == 'I':
        Lista.add_front(entrada[1])
    elif entrada[0] == 'F':
        Lista.add_rear(entrada[1])
    elif entrada[0] == 'P':
        print(Lista.remove_rear())
    elif entrada[0] == 'D':
        print(Lista.remove_front())
    elif entrada[0] == 'E':
        print(Lista.remove_pos(int(entrada[1])))
    elif entrada[0] == 'T':
        Lista.subs(entrada[1], entrada[2])
    else:
        print()

for i in range(Lista.size()):
    print(Lista.remove_front())