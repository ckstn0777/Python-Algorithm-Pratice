
class BinaryTree:
    def __init__(self, left, right):
        self.left = left
        self.right = right


def generateAllBinaryTrees(numNodes):
    result = []
    if numNodes == 0:
        result.append(None)
        return result
    
    for numLeftTreeNodes in range(numNodes):
        numRightTreeNodes = numNodes - 1 - numLeftTreeNodes

        leftSubtrees = generateAllBinaryTrees(numLeftTreeNodes)
        rightSubtrees = generateAllBinaryTrees(numRightTreeNodes)

        # leftSubtrees와 rightSubtress로 이루어진 모든 조합을 생성한다.
        for left in leftSubtrees:
            for right in rightSubtrees:
                result.append(BinaryTree(left, right))
    
    return result


if __name__ == "__main__":
    result = generateAllBinaryTrees(3) # node가 3개인 이진탐색 트리 구조는 몇개일까. 정답은 5이다. 
    print(result[4].left.left)
    print(len(result))