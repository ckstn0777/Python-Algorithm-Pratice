def solution(A):
    A.sort() # 정렬부터 해줌

    maxConstructibleValue = 0

    for a in A:
        if maxConstructibleValue + 1 < a:
            break
        maxConstructibleValue += a

    return maxConstructibleValue + 1


if __name__ == "__main__":
    A = [1, 1, 1, 1, 1, 5, 10, 25] # 21
    #A = [1, 1, 1, 1, 1, 7] # 6

    print(solution(A))