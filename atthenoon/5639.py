#5639 이진 검색 트리
# Node -> 개같이 시간초과
# dictionary -> 역시 시간초과
# 문제의 요구사항 잘 파악할것 트리를 만들라는게 아니라 후위순회 순서로 출력하라는 것
# 문제는 후위순회를 만들라는게 아니라 후위순회가 어떤 순서로 출려되는지 묻는 듯?
# 문제의 input이 전위 순회한 결과라는 것을 알자
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break

def postorder(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1, e+1):
        if tree[s] < tree[i]:
            mid = i
            break
    postorder(s+1, mid-1)
    postorder(mid, e)
    print(tree[s])

postorder(0, len(tree) -1)
# def add(tree, p, c):
#     if tree.get(p) is None:
#         tree[p] = [None, None]
#     if p > c:
#         if tree[p][0]:
#             add(tree, tree[p][0], c)
#         else:
#             tree[p][0] = c
#     else:
#         if tree[p][1]:
#             add(tree, tree[p][1], c) 
#         else:
#             tree[p][1] = c
# def postorder(tree, key):
#     if tree.get(key) and tree[key][0]:
#         postorder(tree, tree[key][0])
#     if tree.get(key) and tree[key][1]:
#         postorder(tree, tree[key][1])
#     print(key)

# root = int(input())
# tree[root] = [None, None]
# while True:
#     try:
#         a = int(input())
#         add(tree, root, a)
#     except:
#         postorder(tree, root)
#         break
