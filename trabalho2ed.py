# Até agr n aceitei, só pode ser meme q isso deu 11 linhas e deu pra fazer em, tipo, alguns minutos. É sério q isso é o trabalho FINAL de ED?
# Nota = 10.00
wookies = [[] for _ in range(int(input()))]
s = []
def wookiezar(i):
    for j in range(len(wookies) + 1):
        if j == len(wookies): s.append(i)
        elif wookies[j][-1] >= i:
            wookies[j].append(i)
            break
[wookies[wookies.index([])].append(i) if [] in wookies else wookiezar(i) for i in map(int, input().split())]
[print("Os Wookies foram para o lado sombrio da força!") if wookies == [] else print(' '.join([str(i) for i in sorted(wookies, key=lambda item: sum(item), reverse=True)]))]
[print("A força está com os Wookies!") if s == [] else print(' '.join(map(str, s)))]