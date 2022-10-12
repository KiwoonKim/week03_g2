#2665 미로만들기

import heapq
import sys
input = sys.stdin.readline
INF = 1e9
size = int(input())
maze = []
for _ in range(size):
    maze.append(list(int(a) for a in input().strip()))
min_count = [[INF] * size for _ in range(size)]
def bfs(x, y):
    global size
    xl = [1, 0, -1, 0]
    yl = [0, 1, 0, -1]
    q = []
    heapq.heappush(q,(0, x, y))
    min_count[x][y] = 0
    while q:
        count, nx, ny = heapq.heappop(q)
        if count > min_count[nx][ny]:
            continue
        for i in range(4):
            next_x = nx + xl[i]
            next_y = ny + yl[i]
            if size > next_x >= 0 and size > next_y >= 0:
                if maze[next_x][next_y] == 1 and min_count[next_x][next_y] > count:
                    min_count[next_x][next_y] = count
                    heapq.heappush(q, (count, next_x, next_y))
                elif maze[next_x][next_y] == 0 and min_count[next_x][next_y] > count + 1:
                    min_count[next_x][next_y] = count + 1
                    heapq.heappush(q, (count + 1, next_x, next_y))
bfs(0, 0)
print(min_count[size-1][size-1])