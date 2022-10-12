#1916 최소비용 구하기

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

cityn = int(input())
busn = int(input())
bus_table = [[] for _ in range(cityn + 1)]
for _ in range(busn):
    frm, to, cost = list(map(int, input().split()))
    bus_table[frm].append((to, cost))
start, dst = list(map(int, input().split()))

min_cost = [INF] * (cityn + 1)
def bfs(start):
    q = []
    heapq.heappush(q,(0, start))
    min_cost[start] = 0
    while q:
        cost, to = heapq.heappop(q)
        if cost > min_cost[to]:
            continue
        for next in bus_table[to]:
            new_cost = cost + next[1]
            if new_cost < min_cost[next[0]]:
                min_cost[next[0]] = new_cost
                heapq.heappush(q, (new_cost, next[0])) 
bfs(start)
print(min_cost[dst])

        # if to == dst:
        #     if cost < min_cost:
        #         min_cost = cost 