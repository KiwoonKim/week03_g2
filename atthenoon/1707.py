#1707 이분 그래프
import sys
# from collections import defaultdict
sys.setrecursionlimit(10**5)
iuput = sys.stdin.readline
putk = int(input())
def dfs(v, c):
    visit[v] = c
    for i in graph[v]:
        if visit[v] * visit[i] == 1: 
            return False
        elif visit[i] == 0:
            ans = dfs(i, -c)
            if not ans: return False
    return True

for _ in range(putk):
    vn, en = list(map(int, input().split()))
    graph = [[] for _ in range(vn+1)]
    for i in range(en):
        frm, to = list(map(int, input().split()))
        graph[frm].append(to)
        graph[to].append(frm)
    visit = [0] * (vn + 1)
    color = 1
    flag = True
    for j in range(1, vn + 1):
        if not visit[j]:
            dfs(j, color)
        if not flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")