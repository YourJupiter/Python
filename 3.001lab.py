for i in range(10):
    print('i =', i)
for i in range(5, 10):
    print('i =', i)
for i in range(5, 10, 2):
    print('i =', i)
for i in range(3):
    response = input('Введіть stop, щоб зупинити цикл (інакше що завгодно): ')
    if response == 'stop':
        break
    else:
        print('Цикл сам був завершений')
print('Кінець програми')
for i in reversed(range(5)):
    print(i)
