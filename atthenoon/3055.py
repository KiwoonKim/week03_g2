#3055 탈출

import sys
from collections import deque

input = sys.stdin.readline
R, C = list(map(int,input().split()))
forest = [[] for _ in range(R)]
water = deque()
start = deque()
for i in range(R):
    j = 0
    l = list(input().strip())
    for s in range(C):
        forest[i].append(l[s])
        if l[s] == 'S':
            start.append((i, j))
        elif l[s] == 'D':
            dst = (i,j)
        elif l[s] == '*':
            water.append((i, j))
        j += 1
    del l
lx = [1, -1, 0, 0]
ly = [0, 0, 1, -1]    
q = deque()
def bfs(w):
    q = deque()
    q.append(w)
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + lx[i]
            ny = y + ly[i]
            if R > ny >= 0 and C > nx >= 0:
                if forest[ny][nx] == '.':
                    forest[ny][nx] = '*'
                    water.append((ny, nx))
def bfs2(s):
    q = deque()
    q.append(s)
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + lx[i]
            ny = y + ly[i]
            if R > ny >= 0 and C > nx >= 0:
                if forest[ny][nx] == '.' or forest[ny][nx] == 'D':
                    forest[ny][nx] = 'S'
                    start.append((ny, nx))
l = len(water)
day = 0
while dst not in start:
    l = len(water)
    for s in range(l):
        bfs(water.popleft())
    l = len(start)
    if l == 0:
        day = 'KAKTUS'
        break
    for _ in range(l):
        bfs2(start.popleft())
    day += 1
print(day)