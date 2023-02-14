import heapq

class Solution(object):
    dx = [-1, 0, 1, 0]
    dy = [0 , -1, 0, 1]

    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.n = len(grid)
        self.distance = [[-1] * self.n for _ in range(self.n)]

        isNotLand = True
        isNotWater = True

        heap = []
        # land는 0으로 바꿔줌
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.distance[i][j] = 0
                    heapq.heappush(heap, (0, i, j))
                    isNotLand = False
                else:
                    isNotWater = False
        
        # land 또는 water가 없는 경우
        if isNotLand or isNotWater:
            return -1
        
        # 0인 녀석(=land)인 경우에 대해 DFS/BFS 조사
        while heap:
            dist, x, y = heapq.heappop(heap)
            # 한번도 탐색이 안된경우 무조건 탐색
            for i in range(4):
                tx = x + Solution.dx[i]
                ty = y + Solution.dy[i]

                if 0 <= tx < self.n and 0 <= ty < self.n and self.distance[tx][ty] == -1:
                    self.distance[tx][ty] = dist + 1
                    heapq.heappush(heap, (dist + 1, tx, ty))
                            
        result = 0
        for i in range(self.n):
            result = max(result, max(self.distance[i]))
        return result


