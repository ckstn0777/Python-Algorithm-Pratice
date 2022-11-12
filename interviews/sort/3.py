
def solution(A):
    A.sort() # 정렬 해주기
    
    writeIdx = 1 # 첫번째 원소는 무조건 존재
    for i in range(1, len(A)):
        if A[i - 1][0] != A[i][0]:
            A[writeIdx] = A[i] 
            writeIdx += 1
    
    return A[0:writeIdx]


if __name__ == "__main__":
    A = [("Ian", "Botham"), ("David", "Gower"), ("Ian", "Bell"), ("Ian", "Chappell")]
    print(solution(A))