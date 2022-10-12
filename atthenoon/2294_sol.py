import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
visited = [0 for _ in range(k+1)] # 방문 시 1, 미방문 시 0

queue = deque()

for coin in coins:
    if coin > k:
        continue
    queue.append((coin, 1)) # (현재까지의 총합, 동전 개수 총합)
    visited[coin] = 1

flag = False # bfs 다 마치고 난 후에도 False이면 해당 합을 만들 수 없는 것이므로 -1 출력

while queue:
    val, cnt = queue.popleft()
    if val == k:
        print(cnt)
        flag = True
        break
    
    for coin in coins:
        if val + coin > k:
            continue
        if visited[val + coin] == 0: # 해당 합에 한번도 방문한 적이 없을 경우 (최단 개수를 구하기 위해)
            queue.append((val + coin, cnt + 1))
            visited[val + coin] = 1

if not flag:
    print(-1)
