# 문제 : 정렬된 배열 두 개가 주어졌을 때, 두 배열에 동시에 존재하는 원소를 새로운 배열 형태로 반환하라. 
# 입력 배열에는 원소가 중복해서 나타날 수 있지만, 반환되는 배열에선 원소가 중복되면 안된다.

def solution(A, B):
    a_pos, b_pos = 0, 0 
    intersectionAB = []

    while len(A) > a_pos and len(B) > b_pos:
        if A[a_pos] == B[b_pos] and (a_pos != 0 and A[a_pos] != A[a_pos - 1]): # 서로 교집합 + 이전 값과 중복되서는 안됨
            intersectionAB.append(A[a_pos])
            a_pos += 1
            b_pos += 1
        elif A[a_pos] < B[b_pos]:
            a_pos += 1
        else: # A[a_pos] > B[b_pos]
            b_pos += 1

    return intersectionAB


if __name__ == "__main__":
    A = [2, 3, 3, 5, 5, 6, 7, 8, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]

    print(solution(A, B)) # [5, 6, 8]이 정답이 되어야 함