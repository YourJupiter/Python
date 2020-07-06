import math
from itertools import count


def f(x, k):
    return pow(-1, k - 1) * ((2 * pow(x, k)) / math.factorial(k))


e = 0.001
a = -3
b = 2
k = 0
i = 0

for x in count(start=a, step=0.5):
    if x > b:
        break
    tmp = f(x, k)
    result = tmp
    ex = pow(math.e, 2*2)
    while abs(tmp) >= e:
        k += 1
        i += 1
        tmp = f(x, k)
        result += x

    print(f"""
x={x}
Результат точно порахованої функції із модуля math: {ex}
Результат: {result}
Точність: {e}
Кількість ітерацій: {k}
{'-' * 10}
    """)
print(f'Загальна кількість ітерацій: {k}')
