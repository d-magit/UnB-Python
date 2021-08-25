pretendentes = [input().split() for _ in range(int(input()))]
pretendentesleve = sorted([[x[0], x[1], x[2],  int(x[3])-75] for x in pretendentes if int(x[3]) - 75 <= 0], key=lambda x: (-(int(x[3])), x[1], x[0]))
pretendentespesado = sorted([[x[0], x[1], x[2], int(x[3])-75] for x in pretendentes if int(x[3]) - 75 > 0], key=lambda x: (x[3], x[1], x[0]))
[print(f'{x[1]}, {x[0]}') for x in sorted(pretendentesleve + pretendentespesado, key=lambda x: abs(int(x[2])-180))]