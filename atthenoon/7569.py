# 7569 토마토

import sys
from collections import deque

input = sys.stdin.readline
lx, ly, lz = map(int, input().split())

tomatopan = [[[0 for _ in range(lx)] for _ in range(ly)] for _ in range(lz)]
ripe = []
empty = 0
for i in range(lz):
    for j in range(ly):
        k = 0
        for a in input().strip().split():
            tomatopan[i][j][k] = int(a)
            if a == '1':
                ripe.append((i, j, k))
            if a == '-1':
                empty += 1
            k += 1
def bfs(xyz : tuple):
    rx = [1, -1, 0, 0, 0, 0]
    ry = [0, 0, 1, -1, 0, 0]
    rz = [0, 0, 0, 0, 1, -1]
    q = deque()
    q.append(xyz)
    while q:
        nz, ny, nx = q.popleft()
        for i in range(6):
            next_x = nx - rx[i]
            next_y = ny - ry[i]
            next_z = nz - rz[i]
            if  lx > next_x >= 0 and ly > next_y >= 0 and lz > next_z >= 0:
                if tomatopan[next_z][next_y][next_x] == 0:
                    tomatopan[next_z][next_y][next_x] = 1
                    ripe.append((next_z, next_y, next_x))
def all_ripe(mat):
    ret = 0
    for j in range(len(mat)):
        for k in range(len(mat[j])):
            ret += sum(mat[j][k])
    return ret
count = 0
l = len(ripe)
last = 0
while l != (lx * ly * lz) - empty:
    prev_l = len(ripe)
    for r in range(last,l):
        bfs(ripe[r])
        last = r
    l = len(ripe)
    count += 1
    if(l == prev_l):
        count = -1
        break
print(count)