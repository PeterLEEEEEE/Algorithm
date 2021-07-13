'''
replace 문자를 아무거나 했다가 계속 출력 오류로 고생함

'''
word = input()
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for words in croatian:
    if words in word:
        word = word.replace(words, '@')


print(len(word))
