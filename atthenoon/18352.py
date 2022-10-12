#18352 특정 거리의 도시 찾기

import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = list(map(int, input().split()))
cities = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = list(map(int, input().split()))
    cities[s].append(e)

visit = set()
ans = []
def bfs(v, limit):
    flag = 0
    queue = deque()
    k = 0
    queue.append((v, k))
    visit.add(v)
    while(queue):
        v, k = queue.popleft()
        k += 1
        if k > limit : break
        for i in cities[v]:
            if i not in visit:
                queue.append((i, k))
                visit.add(i)
                if k == limit:
                    ans.append(i)
                    flag = 1
    if flag == 0:
        print(-1)
    else:
        ans.sort()
        print(*ans, sep='\n')
bfs(X,K)