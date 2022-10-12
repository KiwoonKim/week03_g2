# 1991 트리 순회

# 전위 순회 (루트) (왼쪽자식) (오른쪽자식)

# 후위 순회 (왼쪽자식) (오른쪽자식) (루트)
# 중위 순회 (왼쪽자식) (노드) (오른쪽 자식)

import sys

input = sys.stdin.readline
n = int(input())
t = {}
for i in range(n):
    p, c1, c2 = input().strip().split()
    t[p] = [c1, c2]

def print_mid(root):
    if root != '.':
        print_mid(t[root][0])
        print(root, end='')
        print_mid(t[root][1])


def print_for(root):
    if root != '.':
        print(root, end='')
        print_for(t[root][0])
        print_for(t[root][1])


def print_back(root):
    if root != '.':
        print_back(t[root][0])
        print_back(t[root][1])
        print(root, end='')


print_for('A')
print()
print_mid('A')
print()
print_back('A')
