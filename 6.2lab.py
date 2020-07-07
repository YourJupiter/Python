from collections import Counter
from string import ascii_lowercase

def sort_list(l):
    return sorted(l)
def find_list_element_by_index(l, index):
    try:
        return l[index]
    except IndexError:
        return 'No such element'
def find_chain_in_list(l, chain):
    for i in chain:
        if i not in l:
            return False
    return [i for i in l if i in chain] == [i for i in chain if i in l]
def find_five_min(l):
    return sorted(set(l))[:5]
def find_five_max(l):
    return sorted(set(l))[:-6:-1]
def find_average(l):
    l = [int(i) for i in l]
    return sum(l) / len(l)
def get_list_without_clones(l):
    return set(l)
def run():
    print('Оберіть процедуру, яку хочете виконати:\n'
          '1. Сортування;\n'
          '2. Пошук елементу за значенням;\n'
          '3. Пошук послідовності елементів;\n'
          '4. Пошук перших п’яти мінімальних елементів;\n'
          '5. Пошук перших п’яти максимальних елементів;\n'
          '6. Пошук середнього арифметичного;\n'
          '7. Повернення списку, що сформований з початкового списку, але не'
          'містить повторів (залишається лише перший з однакових елементів)\n'
          '8. stop\n'
          'Введіть номер операції:')
    n = input()
    if n == '1':
        print(sort_list(l))
    elif n == '2':
        print(find_list_element_by_index(l, int(input("Значення: "))))
    elif n == '3':
        print(find_chain_in_list(l, input("Послідовність: ")))
    elif n == '4':
        print(find_five_min(l))
    elif n == '5':
        print(find_five_max(l))
    elif n == '6':
        print(find_average(l))
    elif n == '7':
        print(get_list_without_clones(l))
    elif n == '8':
        exit()
    else:
        print('Перевірте правильність вказаного номеру операції.')

print('Введіть свій список:')
l = list(input())

while True:
    run()
