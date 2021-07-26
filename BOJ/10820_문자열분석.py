import sys

while True:
    n = sys.stdin.readline().rstrip('\n')
    lcnt, ucnt, numcnt, bcnt = 0, 0, 0, 0
    
    if not n:
        break
    for i in n:
        if i.islower():
            lcnt += 1
        elif i.isupper():
            ucnt += 1
        elif i.isdigit():
            numcnt += 1
        elif i.isspace():
            bcnt += 1
        
    print(lcnt, ucnt, numcnt, bcnt)