#2606 바이러스

import sys
input = sys.stdin.readline

putv = int(input())
pute = int(input())
mat = [[0] * (putv+1) for _ in range(putv+1)] 
for i in range(pute):
    x, y = map(int, input().split())
    mat[x][y] = mat[y][x] = 1
visited = [0] * (putv + 1)
def dfs(v):
    visited[v] = 1
    for i in range(1, putv + 1):
        if visited[i] == 0 and mat[v][i]:
            dfs(i)
dfs(1)
print(sum(visited) -1)