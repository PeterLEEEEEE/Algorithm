import math

a = '1+1i'

arr = a.split('+')
a_real = int(arr[0])
a_imag = int(arr[1][:-1])

a = complex(a_real, a_imag)
print(a)

b = '1+1i'

arr = b.split('+')
b_real = int(arr[0])
b_imag = int(arr[1][:-1])

b = complex(b_real, b_imag)
print(b)

c = a * b


print(f'{math.floor(c.real)}+{math.floor(c.imag)}i')
