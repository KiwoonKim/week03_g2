#2573 빙산
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque()
day = 0
check = False

def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    count[x][y] += 1
    return 1

while True:
    visited = [[False]*m for _ in range(n)]
    count = [[0]*m for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
    for i in range(n):
        for j in range(m):
            graph[i][j] -= count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0
    
    if len(result) == 0: # 빙산이 다없어질때까지 분리가 되지않으면 break
        break
    if len(result) >= 2: # 빙산이 분리되면 break
        check = True
        break
    day += 1

if check:        
    print(day)
else:
    print(0)
# import sys
# sys.setrecursionlimit(10**4)
# input = sys.stdin.readline

# row, col = list(map(int, input().split()))
# mat = []
# for i in range(row):
#     mat.append(list(map(int, input().split())))

# def iceberg(m, r, c):
#     def dfs(nextmat, r, c):
#         if mat[r][c] > 0:
#             visit.add((r, c)) 
#             nextmat[r][c] -= checkmelting(m, r, c) 
#             if (r+1, c) not in visit:
#                 dfs(nextmat, r+1, c)
#             if (r, c+1) not in visit:
#                 dfs(nextmat, r, c+1)
#             if (r-1, c) not in visit:
#                 dfs(nextmat, r-1, c)
#             if (r, c-1) not in visit:
#                 dfs(nextmat, r, c-1)

#     def checkmelting(m, row, col):
#         ret = 0
#         if m[row][col+1] <= 0: ret += 1
#         if m[row+1][col] <= 0: ret += 1
#         if m[row-1][col] <= 0: ret += 1
#         if m[row][col-1] <= 0: ret += 1
#         return ret

#     nextmat = [row[:] for row in m]
#     dfs(nextmat, r, c)
#     return nextmat, m

# start = 0
# allout = True
# for i in range(1, row - 1):
#     for j in range(1, col - 1):
#         if mat[i][j] > 0:
#             r = i
#             c = j
#             break
#     else: continue
#     break
# while allout:
#     visit = set()
#     mat, prevmat = iceberg(mat, r, c)
#     for i in range(1,row-1):
#         for j in range(1, col-1):
#             if mat[i][j] > 0:
#                 if (i, j) not in visit:
#                     allout = False
#                     break
#                 r = i
#                 c = j
#         else: continue
#         break

#     if allout == False:
#         break
#     start += 1
#     if not visit:
#         start = 0
#         break
#     del visit

# print(start)