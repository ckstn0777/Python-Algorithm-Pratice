# https://www.acmicpc.net/problem/4195

'''
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
'''

import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        f = int(input())
        parent = dict()
        number = dict()

        for _ in range(f):
            a, b = sys.stdin.readline().strip().split()
            if a not in parent:
                parent[a] = a
                number[a] = 1
            if b not in parent:
                parent[b] = b
                number[b] = 1
            
            union(a, b)
            print(number[find(a)])