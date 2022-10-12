#2617 구슬 찾기
# 단방향이지만 모두 연결 가능성 없음
# 모두 연결이라면 위상정렬 가능?

import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))
wlist = [[] for _ in range(n+1)]
wlist2 = [[] for _ in range(n+1)]
mid = (n+1) // 2
for _ in range(m):
    v1, v2 = list(map(int, input().split()))
    wlist[v1].append(v2)
    wlist2[v2].append(v1)

q = deque()
def dfs(idx, a):
    global count
    for next in a[idx]:
        if visit[next] == 0:
            dfs(next, a)
            count += 1
            visit[next] = 1
res = 0
for i in range(1,n+1): 
    count = 0
    visit = [0] * (n + 1)
    dfs(i, wlist)
    if count >= mid:
        res += 1
    count = 0 
    dfs(i, wlist2)
    if count >= mid:
        res += 1
    

print(res)
