arr = [1,2,3,4,5,6]
temp = 1
flag = 0
for i in range(len(arr)):
    if flag == 1:
        flag = 0
        continue
    else:
        print(i)
    if i == temp:
        flag = 1

