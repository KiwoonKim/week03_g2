#크루스칼 알고리즘

import sys

input = sys.stdin.readline
v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

edges = []  
total_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for i in range(e):
    cost, a, b = edges[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)
#프림 알고리즘

import heapq
import collections
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v, e = map(int, input().split())
graph = collections.defaultdict(list)
visited = [0] * (v+1)

for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, a, b])
    graph[b].append([cost, b, a])

def prim(graph, start_node):
    visited[start_node] = 1
    candidate = graph[start_node]
    heapq.heapify(candidate)
    mst = []
    total_cost = 0
    while candidate:
        cost, a, b = heapq.heappop(candidate)

        if visited[b] == 0:
            visited[b] = 1
            mst.append((a, b))
            total_cost += cost

            for edge in graph[b]:
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)
    return total_cost

print(prim(graph, 1))

