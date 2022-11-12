# 문제 : 정수값이 정렬된 두 개가 있다. 그 중 하나의 배열은 배열 뒤에 충분히 많은 공간이 있어서 두 배열을 정렬된 순서로 합쳐서 저장하는데 사용할 수 있다
# 이 두 배열을 하나로 합쳐 첫 번째 배열에 정렬된 순서로 나열하면 된다. 

def solution(A, B):
    a_pos, b_pos = A.index(None) - 1, len(B) - 1 # 뒤에서부터 비교할거임
    writeIdx = (a_pos + 1) + len(B) - 1 # 어디서부터 쓰기를 하면 되는지 찾음

    while a_pos >= 0 and b_pos >=0:
        if A[a_pos] < B[b_pos]:
            A[writeIdx] = B[b_pos]
            b_pos -= 1
        else:
            A[writeIdx] = A[a_pos]
            a_pos -= 1

        writeIdx -= 1

    # B가 아직 남아있는 경우 합쳐줌. A가 남는 경우는 그냥 그대로 두면 됨(이미 정렬된 상태)
    while b_pos >= 0:
        A[writeIdx] = B[b_pos]
        b_pos -= 1
        writeIdx -= 1

    return A
    


if __name__ == "__main__":
    A = [5, 13, 17, None, None, None, None, None]
    B = [3, 7, 11, 19]

    # A = [1, 2, 5, 7, None, None]
    # B = [3]

    print(solution(A, B))