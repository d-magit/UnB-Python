class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)
      
    def dequeue(self):
       return self.items.pop(0)
    
    def peek(self, pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

entrada = input()
filaoriginal = Queue()
while entrada != '':
    filaoriginal.enqueue(int(entrada))
    entrada = input()

print('Fila geral original')
for i in range(filaoriginal.size()):
    print(str(i+1) + f' - {filaoriginal.peek(i)}')
print('')

print('Fila preferencial')
filapresencial = []
for i in range(filaoriginal.size()):
    if filaoriginal.peek(i) >=  60:
        print(str(i+1) + f' - {filaoriginal.peek(i)}')
        filapresencial.append(i+1)
print('')

print('Fila geral atualizada')
filaatt = []
for i in range(filaoriginal.size()):
    if filaoriginal.peek(i) <  60:
        print(str(i+1) + f' - {filaoriginal.peek(i)}')
        filaatt.append(i+1)
print('')

print('Resultado esperado fila preferencial')
for i in range(len(filapresencial)):
    print(str(i+1) + f' - {filapresencial[i]}')
print('')

print('Resultado esperado fila geral')
for i in range(len(filaatt)):
    print(str(i+1) + f' - {filaatt[i]}')