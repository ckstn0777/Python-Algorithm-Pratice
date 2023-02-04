# https://www.acmicpc.net/problem/1368
'''
4
5
4
4
3
0 2 2 2
2 0 3 3
2 3 0 4
2 3 4 0
'''

# 찾기 연산
def find_parent(parent, x):
  # 루트 노드가 아니라면 루트 노드를 찾을때까지 재귀
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) # 찾으면서 같이 업데이트
  
  return parent[x]

# 합치기 연산
def union_parent(parent, i, j):
  a = find_parent(parent, i)
  b = find_parent(parent, j)

  # 더 큰 번호에 해당하는 노드의 부모를 바꿔주도록 하자
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


if __name__ == "__main__":
  n = int(input())
  parent = [i for i in range(n + 1)] # 부모 테이블(자기 자신으로 초기화)
  edges = []
  
  # i번째 논에 우물을 팔 때 드는 비용 (= 임의의 0이란 정점과 연결된다고 생각하면 됨. 꼼수임)
  for i in range(n):
    edges.append((int(input()), 0, i + 1))
  
  # i - j를 연결하는데 드는 비용
  for i in range(n):
    t_list = list(map(int, input().split()))
    for j in range(n):
      if i < j:
        edges.append((t_list[j], i + 1, j + 1))
  
  # 간선 비용을 오름차순으로 정렬
  edges.sort()

  result = 0

  # 간선을 하나씩 확인하며 
  for edge in edges:
    cost, i, j = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, i) != find_parent(parent, j):
      union_parent(parent, i, j)
      result += cost
  
  print(result)
