name = None #  спочатку  ми  не  знаємо  іменікористувача # нескінчений цикл
while  True:
    print('Меню:')
    print('1.Ввести  ім‘я')
    print('2.  Вивести  привітання')
    print('3.Вийти')
    response  =input('Виберіть  пункт:  ')
    print()
    if response =='1' :
      name  =input('Введіть  ваше  ім‘я:  ')
    elif response  =='2':
      if name: # вітаємося
        print('Привіт,  ',  name,'!',sep='')
      else :
        print('Я  не  знаю  вашого  імені.') 
    elif response  =='3' :
        break
        # оператор break завершує виконання циклуbreak
        #якщо  користувач  вибрав  3,  то  виходимоз циклу
    else:
      print('Неправильне  введення.')
    print()
