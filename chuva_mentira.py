import math
[print(f'{i[0]} / {i[1]}') for i in sorted([(math.ceil(int(y)/int(x)), int(x)) if int(x) != 0 else (0, 0) for x, y in [input().split() for _ in range(int(input()))]], key=lambda x: (-x[0], x[1]))]