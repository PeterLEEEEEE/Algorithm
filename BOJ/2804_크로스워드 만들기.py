def solution(words):
    row_word, col_word = words.split()
    row, col = 0, 0
    arr = [['.']*len(row_word) for _ in range(len(col_word))]

    for i in range(len(col_word)):
        if col_word[i] in row_word:
            row = row_word.index(col_word[i])
            break
    
    for i in range(len(row_word)):
        if row_word[i] in col_word:
            col = col_word.index(row_word[i])
            break

    for i in range(len(arr)):
        arr[i][row] = col_word[i]

    arr[col] = row_word
    
    for i in range(len(arr)):
        print(''.join(arr[i]))


if __name__ == "__main__":
    words = input()
    solution(words)
