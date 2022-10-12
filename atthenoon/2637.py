#2637 장난감 조립
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
M = int(input())
base_toy = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
edges = [[] for _ in range(N+1)]
for i in range(M):
    x, y, z = list(map(int, input().split()))
    edges[x].append((y,z))
    indegree[y] += 1
base = []
q = deque()
for j in range(1, N+1):
    if indegree[j] == 0:
        q.append(j)
    if not edges[j]:
        base.append(j)
base_toy[N] = 1
for i in range(1,N+1):
    if not q:
        print('cycling')
        break
    p = q.popleft()

    for com in edges[p]:
        bupum = com[0]
        cost = com[1]
        base_toy[bupum] += (cost * base_toy[p])
        indegree[bupum] -= 1
        if indegree[bupum] == 0:
            q.append(bupum)
for i in base:
    print(i, base_toy[i])
