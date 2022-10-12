#1260 DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for i in range(n+1)]

visit = [0 for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
# dfs bfs , 모두 visit의 위치를 어디서 넣어줄지 생각하자
# q혹은 스택에 push될때 visit을 넣을지 pop할때 visit에 넣을지 판단 할것

def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n+1):
        if visit[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visit[v] = 0
    while(queue):
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visit[i] == 1 and graph[v][i] == 1:
                queue.append(i)
                visit[i] = 0

dfs(v)
print()
bfs(v)



# import sys
# import collections
# input = sys.stdin.readline
# sys.setrecursionlimit(10000000)
# v, e, s = list(map(int, input().split()))
# graph = collections.defaultdict(list)

# for i in range(e):
#     frm, to = list(map(int, input().split()))
#     graph[frm].append(to)
#     graph[to].append(frm)

# ret = [s]
# def dfs(graph, frm):
#     if len(ret) == len(graph):
#         return ret
#     graph[frm].sort()
#     for i in graph[frm]:
#         if i not in ret:
#             ret.append(i)
#             break
#     dfs(graph, i)
# dfs(graph, s)
# print(*ret)
# visited = []
# def bfs(graph, root):
#     global visited
#     if not visited:
#         visited = [root]
#     for i in graph[root]:
#         if i not in visited:
#             visited.append(i)
#     for k in graph[root]:
#         tmp = k
#         graph[root].pop()
#         bfs(graph, tmp)

#     return visited

# print(*bfs(graph, s))

    
