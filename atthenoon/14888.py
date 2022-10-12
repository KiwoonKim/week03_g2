#14888 연산자 끼워넣기

from copy import copy
import sys
input = sys.stdin.readline

putn = int(input())
putlist = list(map(int, input().split()))
putcal = list(map(int, input().split()))
ans = [-int(1e9), int(1e9)]
def dfs(num, idx, tmp):
    if idx == putn:
        if num > ans[0]:
            ans[0] = num
        if num < ans[1]:
            ans[1] = num
        return
    for a in range(4):
        if tmp[a] > 0:
            tmpc = copy(tmp)
            tmpc[a] -= 1
            if a == 0:
                dfs(num + putlist[idx], idx+1, tmpc)
            elif a == 1:
                dfs(num - putlist[idx], idx+1, tmpc)
            elif a == 2:
                dfs(num * putlist[idx], idx+1, tmpc)
            else:
                a = abs(num) // putlist[idx]
                if num < 0:
                    a *= -1
                dfs(a, idx+1, tmpc)
dfs(putlist[0], 1, putcal)
print(ans[0])
print(ans[1])