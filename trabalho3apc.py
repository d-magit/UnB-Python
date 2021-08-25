# Nota = 8.82
with open(input()) as arquivo:
  lista = arquivo.read().split('\n')
  for i in range(len(lista)):
    if '#' in lista[i]:
      lista[i] = lista[i][0:lista[i].find('#')]
  if lista[0] == 'P1':
    lista = [x for s in [i.split() for i in lista if i != ''] for x in s][3:]
    print(list(''.join(lista)).count('1'))
  elif lista[0] == 'P2':
    lista = [int(x) for s in [i.split() for i in lista[1:] if i != ''] for x in s][2:]
    print(len([i for i in lista[1:] if i > lista[0]/2]))
  else:
    lista = [int(x) for s in [i.split() for i in lista[1:] if i != ''] for x in s][2:]
    val = lista[0]/2
    lista = lista[1:]
    contador = 0
    i = 0
    while i < len(lista):
      media = (lista[i] + lista[i+1] + lista[i+2])/3
      if media > val:
        contador += 1
      i += 3
    print(contador)