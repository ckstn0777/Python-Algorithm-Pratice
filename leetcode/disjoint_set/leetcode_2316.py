class Solution(object):
    def countPairs(self, n, edges):
        def find(parent, a):
            if parent[a] != a:
                parent[a] = find(parent, parent[a])
            return parent[a]
        
        def union(parent, a, b):
            fa = find(parent, a)
            fb = find(parent, b)

            if fa < fb:
                parent[fb] = fa
            else:
                parent[fa] = fb
        
        parent = [i for i in range(n)]

        # union-find 해줌
        for i in range(len(edges)):
            a, b = edges[i]

            if find(parent, a) != find(parent, b):
                union(parent, a, b)
        
        ic = [0 for _ in range(n)]
        for i in range(len(parent)):
            ic[find(parent, parent[i])] += 1
        

        # 몇 개 쌍이 도달할 수 없는지 찾으면 될 듯
        result = 0
        rcnt = sum(ic)
        for i in range(n):
            if ic[i] != 0:
                rcnt -= ic[i]
                result += ic[i] * rcnt

        return result