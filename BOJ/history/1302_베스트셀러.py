from typing import ByteString


n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

books = {}
bestseller = []
for i in arr:
    if i not in books.keys():
        books[i] = 1
    else:
        books[i] += 1

maxnum = max(books.values())
for book, num in books.items():
    if num == maxnum:
        bestseller.append(book)

bestseller.sort()

print(bestseller[0])

