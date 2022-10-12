#2294 동전2

from collections import deque
import sys
input = sys.stdin.readline
N, K = list(map(int,input().split()))
coins = set()

for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.add(coin)
visit = [0 for _ in range(K+1)]

flag = False
q = deque()
q.append((0, 0))
while q:
    coin_n, cost = q.popleft()
    if cost == K:
        flag = True
        minlist = coin_n
        break

    for coin in coins:
        if cost + coin > K:
            continue
        if visit[cost + coin] == 0:
            q.append((coin_n + 1, cost + coin))
            visit[cost + coin] = 1
if flag:
    print(minlist)
else:
    print(-1)
# #2294 동전2

# from collections import deque
# import sys
# import heapq
# input = sys.stdin.readline
# N, K = list(map(int,input().split()))
# coins = []
# for _ in range(N):
#     coin = int(input())
#     if coin <= K:
#         coins.append(coin)

# coins.sort(reverse=True)
# minlist = (K // coins[0]) - 1
# K = K - (minlist * coins[0])
# q = deque()
# visit = set()
# find = 0
# def bfs(coins):
#     global minlist
#     global find
#     q.append((0, 0))
#     while q:
#         coin_n, cost = q.popleft()
#         if cost == K:
#             minlist += coin_n
#             find = 1
#             break
#         for coin in coins:
#             if cost + coin > K:
#                 continue
#             if cost + coin <= K and (coin_n + 1, cost + coin) not in visit:
#                 q.append((coin_n + 1, cost + coin))
#                 visit.add((coin_n + 1, cost+coin))
# bfs(coins)
# if(find):
#     print(minlist)
# else:
#     print(-1)
            



        
            
