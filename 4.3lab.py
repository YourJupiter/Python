text = input("Введіть текст з латинських літер:\n ")
letters = sorted([i for i in text.lower() if i in 'aeiouy'])
for i in letters:
    print(i, end=' ')
