# Nota = 10.00
tabela = [['b','c','x','f','k','s'],['f','g','y','s'],['n','b','c','g','r','p','u','e','w','y'],['t','f'],['a','l','c','y','f','m','n','p','s'],['a','d','f','n'],['c','w','d'],['b','n'],['k','n','b','h','g','r','o','p','u','e','w','y'],['e','t'],['b','c','u','e','z','r','?'],['f','y','k','s'],['f','y','k','s'],['n','b','c','g','o','p','e','w','y'],['n','b','c','g','o','p','e','w','y'],['p','u'],['n','o','w','y'],['n','o','t'],['c','e','f','l','n','p','s','z'],['k','n','b','h','r','o','u','w','y'],['a','c','n','s','v','y'],['g','l','m','p','u','w','d']]
K = int(input())
Ntrain, Ntest = [int(i) for i in input().split()]
cogumelos = [[i for i in input().split()] for _ in range(Ntrain)]
for i in range(Ntrain):
  for x in range(22):
    cogumelos[i][x] = tabela[x].index(cogumelos[i][x])
medias = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
desvios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(22):
  for i in range(Ntrain):
    medias[x] += cogumelos[i][x]
  medias[x] /= Ntrain
  for i in range(Ntrain):
    desvios[x] += (cogumelos[i][x] - medias[x])**2
  desvios[x] = (desvios[x]/Ntrain)**(1/2)
  if desvios[x] == 0:
    for i in range(Ntrain):
      cogumelos[i][x] = 0
  else:
    for i in range(Ntrain):
      cogumelos[i][x] -= medias[x]
      cogumelos[i][x] /= desvios[x]
rotulos = [input() for _ in range(Ntrain)]
testes = [[i for i in input().split()] for _ in range(Ntest)]
for i in range(Ntest):
  for x in range(22):
    testes[i][x] = tabela[x].index(testes[i][x])
for x in range(22):
  if desvios[x] == 0:
    for i in range(Ntest):
      testes[i][x] = 0
  else:
    for i in range(Ntest):
      testes[i][x] -= medias[x]
      testes[i][x] /= desvios[x]
for i in range(Ntest):
  distancias = {}
  contador = {'e': 0, 'p': 0}
  for x in range(Ntrain):
    distancias[x] = 0
    for y in range(22):
      distancias[x] += (testes[i][y] - cogumelos[x][y])**2
    distancias[x] = distancias[x]**(1/2)
  distancias = list({k: v for k, v in sorted(distancias.items(), key=lambda item: item[1], reverse=True)})
  for i in range(1, K+1):
    if rotulos[distancias[-i]] == 'e':
      contador['e'] += 1
    else:
      contador['p'] += 1
  if contador['e'] >= contador['p']:
    print('e')
  else:
    print('p')