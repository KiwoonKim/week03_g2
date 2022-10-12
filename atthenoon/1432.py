#1432 그래프 수정

import sys
from collections import deque
import heapq
input = sys.stdin.readline
# 위상정렬은 선후 관계가 명확하지 않은 노드들에 대해선 정렬을 하지 않는다.
# 일반적인 큐 대신 heapq를 사용하여 출력되는 결과들을 정렬하여 출력할 수 있다.

N = int(input())
graph = [[] for _ in range(N+1)]
nlist = [0 for _ in range(N+1)]
outdeg = [0 for _ in range(N+1)]
for i in range(N):
    for j, v in enumerate(input().strip()):
        if v == '1':
            graph[j+1].append(i+1)
            outdeg[i+1] += 1
q = []
for i in range(N, 0, -1):
    if outdeg[i] == 0:
        heapq.heappush(q, -i)
n = N
flag = 1
for j in range(N, 0, -1):
    if not q:
        flag = 0
        break
    p = -heapq.heappop(q)
    nlist[p] = n
    n -= 1
    for j in reversed(graph[p]):
        next = j
        outdeg[next] -= 1
        if outdeg[next] == 0:
            heapq.heappush(q,-next)
if flag:
    print(*nlist[1:])
else:
    print(-1)