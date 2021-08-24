pool = [1, 8, 6, 2, 5, 4, 8, 3, 7]

first, last = 0, len(pool) - 1
max_volumn = 0

while first < last:

    height = min(pool[first], pool[last])
    width = last - first
    if max_volumn < (height * width):
        max_volumn = height * width

    if first < last:
        first += 1
    elif first > last:
        last -= 1

print(max_volumn)
