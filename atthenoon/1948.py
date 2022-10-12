#1948 임계경로

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
indeg = [0 for _ in range(n+1)]
time_sum = [0 for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]

for i in range(m):
    s, e, c = list(map(int,input().split()))
    graph[s].append([e, c])
    back_graph[e].append([s, c])
    indeg[e] += 1

start, dst = list(map(int, input().split()))

q = deque()
# q.append(start)
for i in range(1, n+1):
    if indeg[i] == 0:
        q.append(i)
while q:
    cur = q.popleft()
    for ncity, time in graph[cur]:
        time_sum[ncity] = max(time_sum[ncity], time_sum[cur] + time)
        indeg[ncity] -= 1
        if indeg[ncity] == 0:
            q.append(ncity)
            
cnt = 0
q = deque()
q.append(dst)
visit = [0] * (n+1)
while q:
    idx = q.popleft()
    # visit[idx] = 1 과 다음 값에 append할 때 visit을 해주는 것의 차이가 무엇인가.
    for prev, t in back_graph[idx]:
        if time_sum[prev] + t == time_sum[idx]:
            cnt += 1
            if visit[prev] == 0:
                q.append(prev)
                visit[prev] = 1
print(time_sum[dst])
print(cnt)