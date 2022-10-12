#2178 미로 탐색

import sys
from collections import deque
input = sys.stdin.readline
row, col = list(map(int, input().split()))
maze = []
for _ in range(row):
    maze.append([int(a) for a in (input().strip())])

visit = set ()
def bfs(r, c, min_xy):
    d = 0
    queue = deque()
    queue.append((r, c, d))
    visit.add((r, c))
    while(queue):
        y, x, d = queue.popleft()
        d += 1
        if y == row - 1 and x == col - 1:
            min_xy = d if min_xy > d else min_xy
            break
        if y - 1 >= 0 and (y - 1, x) not in visit and maze[y - 1][x] == 1:
            queue.append((y - 1, x, d))
            visit.add((y-1, x))
        if x + 1 < col and (y, x + 1) not in visit and maze[y][x + 1] == 1:
            queue.append((y, x  + 1, d))
            visit.add((y, x + 1))
        if y + 1 < row and (y + 1, x) not in visit and maze[y + 1][x] == 1:
            queue.append((y+1, x, d))
            visit.add((y+1, x))
        if x - 1 >= 0 and (y, x - 1) not in visit and maze[y][x - 1] == 1:
            queue.append((y, x - 1, d))
            visit.add((y, x - 1))
    return min_xy
print(bfs(0,0, row * col))
