import random
n = int(input('Введіть кількість елементів списку n: \n'))
spysok=random.sample(range(0,50),n)
print('Згенерований список:',spysok)

sum=0
for i in range(len(spysok)):
    if spysok[i]%2==1 :
        sum=sum+spysok[i]
print('Сума непарних чисел: ',sum)
