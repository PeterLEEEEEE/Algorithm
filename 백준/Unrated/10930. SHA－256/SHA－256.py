import sys
import hashlib

input = sys.stdin.readline

S = input().rstrip()

sha = hashlib.sha256()
sha.update(S.encode())

ans = str(sha.hexdigest())

print(ans)