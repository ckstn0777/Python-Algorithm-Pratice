class Solution(object):
    def DFS(self, node, direct, path_cnt):
        if node.right:
            if direct == 'L': # 다음 Right가 있고 이전에 Left에서 왔다면 
                self.DFS(node.right, 'R', path_cnt + 1)
            else: # 해당 node부터 시작할 경우
                self.answer = max(self.answer, path_cnt)
                self.DFS(node.right, 'R', 1)
        else: # 끝인 경우 (종료)
            self.answer = max(self.answer, path_cnt)

        if node.left:
            if direct == 'R':
                self.DFS(node.left, 'L', path_cnt + 1)
            else:
                self.answer = max(self.answer, path_cnt)
                self.DFS(node.left, 'L', 1)
        else: # 끝인 경우 (종료)
            self.answer = max(self.answer, path_cnt)


    def longestZigZag(self, root):
        self.answer = 0

        # DFS
        # root부터 왼쪽, 오른쪽 탐색? 
        
        if root.left:
            self.DFS(root.left, 'L', 1)
        
        if root.right:
            self.DFS(root.right, 'R', 1)

        
        return self.answer