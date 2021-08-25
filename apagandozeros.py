strings = [list(input()) for i in range(int(input()))]
for i in strings:
    nzeros = 0
    x = 0
    while x != len(i)-1:
        if i[x] == '1' and ('1' in i[x+1:]) == True:
            while i[x + 1] != i[x]:
                if x+1 != len(i)-1:
                    i.pop(x + 1)
                    nzeros += 1
                else:
                    i.pop(x + 1)
                    nzeros += 1
                    break
        x += 1
    print(nzeros)