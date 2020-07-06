phonebook = { 'Олександр': '123-032-846', 'Анатолій': '432-917-333', 'Вадим': '345-120-422', 'Андрій': '111-890-532',     } 
print(phonebook['Вадим'])
phonebook['Андрій']  = '222-890-532'
phonebook['Олег']  = '432-850-133'
print(phonebook, '\n', len(phonebook), 'entries  found')
for person in ('Анатолій', 'Вадим', 'Микола'):
    if person in phonebook:
     print(person, 'is  in  the  phonebook')
    else:
     print('No  entry  found  for',  person)
