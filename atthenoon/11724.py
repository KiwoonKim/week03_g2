#11724  연결 요소의 개수

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

vn, en = map(int, input().split())
graph = [[0] * (vn + 1) for _ in range(vn+1)]
for _ in range(en):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

count = 0
visit = [0] * (vn + 1)
visitlist = []
def dfs(v):
    visit[v] = 1
    visitlist.append(v)
    for i in range(1, vn+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)

for i in range(1, vn+1):
    if visit[i] == 0:
        dfs(i)
        count+=1
print(count + vn - len(visitlist))