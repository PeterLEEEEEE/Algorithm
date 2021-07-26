import string

n = input()
low_alpha = string.ascii_lowercase
upper_alpha = string.ascii_uppercase
nums = ['0','1','2','3','4','5','6','7','8','9']
ans = []

for i in n:
    if i == ' ':
        ans.append(' ')
    if i in nums:
        ans.append(i)
    elif i in low_alpha:
        tmp = low_alpha.index(i)
        if tmp > 12:
            ans.append(low_alpha[tmp-13])
        else:
            ans.append(low_alpha[tmp+13])
    elif i in upper_alpha:
        tmp = upper_alpha.index(i)
        if tmp > 12:
            ans.append(upper_alpha[tmp-13])
        else:
            ans.append(upper_alpha[tmp+13])

print(''.join(ans))