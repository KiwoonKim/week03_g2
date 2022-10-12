#11725 트리의 부모 찾기
import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
putsize = int(input())
graph = [[] for _ in range(putsize + 1 ) ] 
visit = [0] * (putsize + 1)
visited_list = [[] for _ in range(putsize + 1)]

for i in range(1, putsize):
    x, y = list(map(int, input().split()))
    graph[y].append(x)
    graph[x].append(y)
def dfs(v):
    visit[v] = 1
    for i in graph[v]:
        if visit[i] == 0:
            visited_list[i] = v
            dfs(i)

for i in range(1, putsize + 1):
    dfs(i)
for i in range(2, len(visited_list)):
    print(visited_list[i])