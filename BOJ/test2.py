n = 20

n = bin(n)[2:]
print(n)
flag = 0
cnt = 0
for i in n:
    if flag == 0 and i == 1:
        flag = 1

    if flag == 1:
        cnt += 1
# arr.insert(0, 0)
# arr.append(0)
# max_len = 0
# for i in range(1, len(arr)-1):
#     if arr[i-1] == '' and arr[i+1] == '':
#         max_len = max(max_len, len(arr[i]))

# print(max_len)