from os import listdir

def read_file():
    with open('students.txt') as file:
        data = file.readlines()
        for i in data:
            i = i.split(',')
            print(f"Ім'я: {i[0]}, Середній бал: {i[1]}", end='')

def add_to_file():
    with open('students.txt', 'a') as file:
        name = input("\nІм'я: ")
        grade = input("Середній бал: ")
        file.write(f"\n{name},{grade}")

def find_file():
    filename = input("Вкажіть ім'я файлу: ")
    results = [file for file in listdir('.') if filename in file]
    if len(results) > 0:
        for i in results:
            print(i)
    else:
        print("Нічого не знайдено")

def find_in_file():
    with open('students.txt') as file:
        data = file.readlines()
        query = input("Що ви хочете знайти?: ")
        for line in data:
            if query in line:
                print(line)
                
def run():
    print('\nОберіть процедуру, яку хочете виконати:\n'
          '1. Читання файлу;\n'
          '2. Запис у файл;\n'
          '3. Пошук файлів у каталозі;\n'
          '4. Пошук даних в файлі;\n'
          '5. Stop\n'
          'Введіть номер операції:')
    n = input()
    if n == '1':
       read_file()
    elif n == '2':
        add_to_file()
    elif n == '3':
        find_file()
    elif n == '4':
        find_in_file()
    elif n == '5':
        exit()
    else:
        print('Перевірте правильність вказаного номеру операції.')

while True:
    run()
