from collections import Counter
print('Введіть перше слово:')
word1 = input()
print('Введіть друге слово:')
word2 = input()

print(False if Counter(word2) - Counter(word1) else True)
