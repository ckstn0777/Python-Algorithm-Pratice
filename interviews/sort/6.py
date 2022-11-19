
def solution(A, B):
    result = []
    i = 0
    
    # B 보다 앞에 등장하는 구간에 대해 처리 한다.
    while i < len(A) and B[0] > A[i][1]:
        result.append(A[i])
        i += 1
    
    # 겹치는 구간에 대해 처리
    newInterval = [B[0], B[1]]
    while i < len(A) and B[1] >= A[i][0]:
        # 만약 [a, b]와 [c, d]가 겹친다면, 이들을 합친 결과는 [min(a, c), max(b, d)]가 된다. 
        newInterval = [min(newInterval[0], A[i][0]), max(newInterval[1], A[i][1])]
        i += 1

    result.append(newInterval)
    
    # B 보다 뒤에 등장하는 구간에 대해 처리 한다. (그냥 이후에는 합쳐주면 됨)
    result = result + A[i:]
    
    return result


if __name__ == "__main__":
    #A = [[-4, -1], [0, 2], [3, 6], [7, 9], [11, 12], [14, 17]]
    #B = [1, 8]

    A = [[-4, -1], [0, 2], [3, 5], [8, 9], [11, 12], [14, 17]]
    B = [6, 7]
    print(solution(A, B))