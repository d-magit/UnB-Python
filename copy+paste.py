import math
bytesrestantes = int(input())
print(f'Transmitindo {bytesrestantes} bytes...')
velm = 0
i = 0
while bytesrestantes != 0:
    i += 1
    vel = int(input())
    bytesrestantes -= vel
    velm += vel/5
    if bytesrestantes != 0:
        if velm != 0 and i % 5 == 0:
            print('Tempo restante: {tempo}'.format(tempo = math.ceil(float(f'{bytesrestantes/velm:1.4f}'))) + ' segundos.')
            velm = 0
        elif i % 5 == 0:
            print('Tempo restante: pendente...')
print(f'Tempo total: {i} segundos.')