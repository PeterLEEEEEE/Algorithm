word = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for words in croatian:
    if words in word:
        word = word.replace(words, '@')


print(len(word))
