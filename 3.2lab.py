import random
n = int(input('Введіть кількість рядків матриці n: \n'))
m = int(input('Введіть кількість стовбців матриці m:\n'))

print('Згенерована матриця:')

from random import randint
matr =[[randint(-10, 10) for j in range(n)] for i in range(m)]
print(matr)

print('Мінімальний елемент матриці:')

xi=0
xj=0

for i in range(len(matr)):
    for j in range(len(matr[i])):
        if matr[i][j] > 0:
            mine=matr[i][j]
            break

for i in range(len(matr)):
    for j in range(len(matr[i])):
        if matr[i][j] > 0:
            if matr[i][j]<mine:
                mine=matr[i][j]
                xi=i
                xj=j
print(mine, '\nРозташування мінімального елемента:\nСтовбець:', xi, 'Рядок:', xj)

if xi==m-1:
    print('Мінімальний елемент знаходиться у останньому стовбці')
else:
    for j in range(len(matr)):
        temp=matr[xi][j]
        matr[xi][j]=matr[m-1][j]
        matr[m-1][j]=temp
print('Перетворена матриця:\n',matr)
    
