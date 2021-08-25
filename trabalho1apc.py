# Nota = 10.00
import datetime
T = input()
N = int(input())
list1 = [input().split() for _ in range(N)]
NU_ANO_INGRESSO, NU_DIA_NASCIMENTO, NU_MES_NASCIMENTO, NU_ANO_NASCIMENTO, TP_SEXO, TP_SITUACAO = [[int(i[x]) for i in list1] for x in range(6)]
if T == '1':
  regulares = TP_SITUACAO.count(2) + TP_SITUACAO.count(6)
  print(f'matriculados ou formados:{100*regulares/len(TP_SITUACAO):5.1f}', f'alunos em outras situacoes:{100*(1-regulares/len(TP_SITUACAO)):5.1f}', sep='\n')
elif T == '2':
  femininos = TP_SEXO.count(1)
  print(f'sexo masculino:{100*(1-femininos/len(TP_SEXO)):5.1f}', f'sexo feminino:{100*(femininos/len(TP_SEXO)):5.1f}', sep='\n')
elif T == '3':
  somaanos = 0
  for i in NU_ANO_INGRESSO:
    somaanos += i
  print(f'media de anos desde ingresso:{(2019*len(NU_ANO_INGRESSO)-somaanos)/len(NU_ANO_INGRESSO):5.1f}')
elif T == '4':
  segunda = 0
  terca = 0
  quarta = 0
  quinta = 0
  sexta = 0
  sabado = 0
  domingo = 0
  for i in range(N):
    dia = datetime.datetime(NU_ANO_NASCIMENTO[i], NU_MES_NASCIMENTO[i], NU_DIA_NASCIMENTO[i]).weekday()
    if dia == 0:
      segunda += 1
    elif dia == 1:
      terca += 1
    elif dia == 2:
      quarta += 1
    elif dia == 3:
      quinta += 1
    elif dia == 4:
      sexta += 1
    elif dia == 5:
      sabado += 1
    elif dia == 6:
      domingo += 1 
  print(f'domingo:{100*domingo/N:5.1f}', f'segunda:{100*segunda/N:5.1f}', f'terca:{100*terca/N:5.1f}', f'quarta:{100*quarta/N:5.1f}', f'quinta:{100*quinta/N:5.1f}', f'sexta:{100*sexta/N:5.1f}', f'sabado:{100*sabado/N:5.1f}', sep='\n')
elif T == '5':
  masculinos = [x for x, y in enumerate(TP_SEXO) if y == 2]
  femininos = [x for x, y in enumerate(TP_SEXO) if y == 1]
  regularesm = 0
  for i in masculinos:
    if TP_SITUACAO[i] == 2 or TP_SITUACAO[i] == 6:
      regularesm += 1
  print('dentre masculinos:', f'matriculados ou formados:{100*regularesm/len(masculinos):5.1f}', f'alunos em outras situacoes:{100*(1-regularesm/len(masculinos)):5.1f}', sep='\n')
  regularesf = 0
  for i in femininos:
    if TP_SITUACAO[i] == 2 or TP_SITUACAO[i] == 6:
      regularesf += 1
  print('dentre femininos:', f'matriculados ou formados:{100*regularesf/len(femininos):5.1f}', f'alunos em outras situacoes:{100*(1-regularesf/len(femininos)):5.1f}', sep='\n')
elif T == '6':
  regulares = [x for x, y in enumerate(TP_SITUACAO) if y == 2 or y == 6]
  irregulares = [x for x, y in enumerate(TP_SITUACAO) if y != 2 and y != 6]
  anostotaisreg = 0
  for i in regulares:
    anostotaisreg += NU_ANO_INGRESSO[i]
  print('dentre matriculados ou formados:', f'media de anos desde ingresso:{(2019*len(regulares)-anostotaisreg)/len(regulares):5.1f}', sep='\n')
  anostotaisirreg = 0
  for i in irregulares:
    anostotaisirreg += NU_ANO_INGRESSO[i]
  print('dentre alunos em outras situacoes:', f'media de anos desde ingresso:{(2019*len(irregulares)-anostotaisirreg)/len(irregulares):5.1f}', sep='\n')
else:
  masculinos = [x for x, y in enumerate(TP_SEXO) if y == 2]
  femininos = [x for x, y in enumerate(TP_SEXO) if y == 1]
  segundam = 0
  tercam = 0
  quartam = 0
  quintam = 0
  sextam = 0
  sabadom = 0
  domingom = 0
  for i in masculinos:
    dia = datetime.datetime(NU_ANO_NASCIMENTO[i], NU_MES_NASCIMENTO[i], NU_DIA_NASCIMENTO[i]).weekday()
    if dia == 0:
      segundam += 1
    elif dia == 1:
      tercam += 1
    elif dia == 2:
      quartam += 1
    elif dia == 3:
      quintam += 1
    elif dia == 4:
      sextam += 1
    elif dia == 5:
      sabadom += 1
    elif dia == 6:
      domingom += 1 
  print('dentre masculinos:', f'domingo:{100*domingom/len(masculinos):5.1f}', f'segunda:{100*segundam/len(masculinos):5.1f}', f'terca:{100*tercam/len(masculinos):5.1f}', f'quarta:{100*quartam/len(masculinos):5.1f}', f'quinta:{100*quintam/len(masculinos):5.1f}', f'sexta:{100*sextam/len(masculinos):5.1f}', f'sabado:{100*sabadom/len(masculinos):5.1f}', sep='\n')
  segundaf = 0
  tercaf = 0
  quartaf = 0
  quintaf = 0
  sextaf = 0
  sabadof = 0
  domingof = 0
  for i in femininos:
    dia = datetime.datetime(NU_ANO_NASCIMENTO[i], NU_MES_NASCIMENTO[i], NU_DIA_NASCIMENTO[i]).weekday()
    if dia == 0:
      segundaf += 1
    elif dia == 1:
      tercaf += 1
    elif dia == 2:
      quartaf += 1
    elif dia == 3:
      quintaf += 1
    elif dia == 4:
      sextaf += 1
    elif dia == 5:
      sabadof += 1
    elif dia == 6:
      domingof += 1 
  print('dentre femininos:', f'domingo:{100*domingof/len(femininos):5.1f}', f'segunda:{100*segundaf/len(femininos):5.1f}', f'terca:{100*tercaf/len(femininos):5.1f}', f'quarta:{100*quartaf/len(femininos):5.1f}', f'quinta:{100*quintaf/len(femininos):5.1f}', f'sexta:{100*sextaf/len(femininos):5.1f}', f'sabado:{100*sabadof/len(femininos):5.1f}', sep='\n')