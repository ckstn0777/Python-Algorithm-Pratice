# https://www.acmicpc.net/problem/1135
'''
5
-1 0 0 2 2
'''


if __name__ == "__main__":
  n = int(input())
  t_list = list(map(int, input().split()))

  tree = [[] for _ in range(n)]
  for i in range(1, n):
    tree[t_list[i]].append(i) # t_list[i]의 자식은 i
  
  child_cnt = [0] * n # 자식 카운트

  def dp(v):
    child_node = []

    if len(tree[v]) == 0:
      child_cnt[v] = 0
    else:
      for child in tree[v]:
        dp(child) # 계속 재귀 탐색
        child_node.append(child_cnt[child])

      # 모든 자식 노드의 딸린 자식의 카운트 집계 후 내림차순 정렬
      child_node.sort(reverse=True)
      # 자식이 많은 순으로 계속 1씩 증가시켜서 더함(=연락을 하는거지. 순서대로)
      child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
      child_cnt[v] = max(child_node)

  dp(0)
  print(child_cnt[0])

  

