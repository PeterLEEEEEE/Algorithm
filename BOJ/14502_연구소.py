# 미완성
import sys, copy
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def set_wall():
    pass


N, M = map(int, input().split())
lab_list = []
for _ in range(N):
    lab_list.append(list(map(int, input().split())))


set_wall(0,0)
