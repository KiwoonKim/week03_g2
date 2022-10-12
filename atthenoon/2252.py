#2252 줄 세우기
#위상 정렬문제
# 두학생의 키를 비교 -> A 학생과 B학생의 일방향 그래프
# 역행은 존재하지 않음 1 3 이면 3 이 1보다 항상 크다는 것이기 때문
# 이는 위상 정렬을 할 수 있는 조건

import sys
from collections import deque
input = sys.stdin.readline
N, M = list(map(int, input().split()))
key = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for i in range(1, M + 1):
    a , b = list(map(int,input().split()))  
    key[a].append(b)
    indegree[b] += 1

q = deque()
ret = []
for j in range(1, N + 1):
    if(not indegree[j]):
        q.append(j)
    
for k in range(1, N+1):
    if not q:
        print('cycle')
        break
    node = q.popleft()
    ret.append(node)
    for next in key[node]:
        indegree[next] -= 1
        if not indegree[next]:
            q.append(next)
print(*ret)