# 문제 : 최종 점수와 각 게임에서 낼 수 있는 점수가 주어졌을 때, 주어진 최종 점수를 만들 수 있는 조합의 개수를 반환하라
# 예를 들어, [2점, 3점, 7점]으로 12점을 만들 수 있는 조합의 개수는 4이다. 
'''
12
2 3 7
'''

# 해결방법 : 간단하게 각 경기에 2점 혹은 3점을 낼 수 있고 총 6점을 만드는 조합의 수를 계산한다고 해보자.
# 이는 곰곰히 생각해보면 (2점으로 6점을 만드는 방법) + (2, 3점으로 3점을 만드는 방법) 이 된다.
# A[1][6] = A[0][6] + A[1][3] 이 되는데 이를 일반화 하면 A[i][j] = A[i - 1][j] + A[i][j - 추가된 점수(3)]

# 시간복잡도는 O(sn), 공간복잡도 또한 O(sn)이다. s는 점수, n는 주어진 점수들.... 
def numCombinationsForFinalScore(finalScore, individualPlayScores):
    numCombinationsForScore = [[0] * (finalScore + 1) for _ in range(len(individualPlayScores))]
    
    for i in range(len(individualPlayScores)):
        numCombinationsForScore[i][0] = 1 # 0점이 될 수 있는 방법의 개수는 1로 초기화
        for j in range(1, finalScore + 1):
            withoutThisPlay = numCombinationsForScore[i - 1][j] if i - 1 >= 0 else 0
            withThisPlay = numCombinationsForScore[i][j - individualPlayScores[i]] if j >= individualPlayScores[i] else 0

            numCombinationsForScore[i][j] = withoutThisPlay + withThisPlay
    
    return numCombinationsForScore[len(individualPlayScores) - 1][finalScore]


if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))

    print(numCombinationsForFinalScore(n, scores))
    