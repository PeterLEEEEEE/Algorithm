import sys
while True:
    n = sys.stdin.readline().rstrip()
    if n == 'END':
        break

    print(n[::-1])