# Obs.: If the number is a positive complement, for example, 0100, it should be treated as a Signal and Magnitude, therefore, an 's' should be added to the end of the base.

# Estabelece a lista de dígitos e as variáveis necessárias
lista = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
var1 = input("Type the first base, followed by 's' if it's a Signal and Magnitude number: ")
var2 = input("Type the number: ")
var3 = input("Type the second base, followed by 's' if the desired result is in Signal and Magnitude: ")
ncasas = input("Type the number of fractionary digits, this will be rounded up if necessary: ")
def converter(baseA, numero, baseB, ncasas):
  resultado = ''
  valor = 0
  # Define se o resultado é negativo
  if '-' in numero:
    resultado += '-'
    numero = numero[1:]
  # Define se haverá parte fracionária
  if '.' in numero:
    numero = numero.split('.')
    numeroint = numero[0][::-1]
    if numero[1] == '0':
      numerofrac = False
    else:
      numerofrac = numero[1]
  else:
    numeroint = numero[::-1]
    numerofrac = False
  # Converte a parte inteira para base 10
  for i in range(len(numeroint)):
    valor += lista.index(numeroint[i])*(int(baseA)**i)
  if valor == 0:
    resultado += '0'
  # Converte a parte inteira da base 10 para a base final
  inteiros = []
  while valor != 0:
    inteiros.insert(0, lista[valor%int(baseB)])
    valor = valor//int(baseB)
  resultado += ''.join(inteiros)
  # Converte a parte fracionária para a base 10
  if numerofrac:
    resultado += '.'
    ncasas = int(ncasas)
    for i in range(len(numerofrac)):
      valor += (lista.index(numerofrac[i]))/(int(baseA)**(i + 1))
    # Converte a parte fracionária da base 10 pra base final e arredonda
    while valor > 0 and ncasas > 0:
      valor *= int(baseB)
      partefrac = valor - int(valor)
      if ncasas == 1:
        if partefrac >= 0.5:
          resultado += lista[int(valor + 1)]
        else:
          resultado += lista[int(valor)]
      else:
        resultado += lista[int(valor)]
      ncasas -= 1
      valor -= int(valor)
      while lista.index(resultado[resultado.find('.')+1:][-1]) == int(baseB):
        if resultado[-2] == '.':
          resultado = resultado[:-3] + lista[lista.index(resultado[-3]) + 1]
          resultado = converter(baseB, resultado, baseB, 10000)
        else:
          resultado = resultado[:-2] + lista[int(lista.index(resultado[-2])) + 1]
  if resultado == '-' or resultado == '':
    return '0'
  return resultado
signal = None
# Checa se a 1ª base é sinal e magnitude
if 's' in var1:
  var1 = var1[0:-1]
  var2 = converter(var1, var2, 10, 10000)
else:
  if '.' in var2:
    tempvar = var2[0:var2.index('.')]
  else:
    tempvar = var2
  if var2 != '0':
    var2 = str(-1*(float(converter(var1, str(10**len(tempvar)), 10, 10000)) - float(converter(var1, var2, 10, 10000))))
  if 'e' in var2:
    isneg = 0
    if '-' in var2:
      isneg = 1
      var2 = var2[1:]
    var2 = '-'*isneg + '0.'+ '0'*(int(var2[var2.find('e')+2:])-1) + ''.join(var2[:var2.find('e')].split('.'))
    del isneg
if 's' in var3:
  signal = True
  var3 = var3[0:-1]
var2 = converter(10, var2, var3, ncasas)
if signal:
  print('\nResult: ' + var2)
else:
  if '-' in var2:
    var2 = var2[1:]
  if '.' in var2:
    tempvar = var2[0:var2.index('.')]
  else:
    tempvar = var2
  if float(var2) != 0:
    var2 = str(float(converter(var3, str(10**(len(tempvar) + 1)), 10, 10000)) - float(converter(var3, var2, 10, 10000)))
  if 'e' in var2:
    isneg = 0
    if '-' in var2:
      isneg = 1
      var2 = var2[1:]
    var2 = '-'*isneg + '0.'+ '0'*(int(var2[var2.find('e')+2:])-1) + ''.join(var2[:var2.find('e')].split('.'))
    del isneg
  print('\nResult: ' + converter(10, var2, var3, 10000))