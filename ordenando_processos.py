class Pile:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def pile(self, item):
        self.__items.append(item)

    def unpile(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def isSorted(self):
        return sorted(self.__items, reverse=True) == self.__items

a = Pile()
b = Pile()
_ = input()
counter = 0
[a.pile(i) for i in input().split()]
for i in reversed(range(a.size())):
    hand = a.unpile()
    for j in range(i):
        current = a.unpile()
        if hand < current:
            b.pile(hand)
            hand = current
        else:
            b.pile(current)
    b.pile(hand)
    for j in range(b.size()):
        a.pile(b.unpile())
    counter += 1
    if a.isSorted():
        break
print(counter)