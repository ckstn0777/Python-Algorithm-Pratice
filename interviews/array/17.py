

def hasDuplicate(arr, start_row, end_row, start_col, end_col):
    is_present = [False] * (len(arr) + 1)
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            
            if arr[i][j] != 0 and is_present[arr[i][j]]:
                return True

            is_present[arr[i][j]] = True

    return False


def isValidSudoku(arr):
    # 행 제한사항 확인
    for i in range(9):
        if hasDuplicate(arr, i, i + 1, 0, len(arr[i])):
            return False

    # 열 제한사항 확인
    for j in range(9):
        if hasDuplicate(arr, 0, len(arr), i, i + 1):
            return False

    # 격자판 제한사항 확인
    for I in range(3):
        for J in range(3):
            if hasDuplicate(arr, 3 * I, 3 * (I + 1), 3 * J, 3 * (J + 1)):
                return False
    
    return True


if __name__ == "__main__":
    # 9 X 9 스도쿠가 있다고 하자
    arr = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print(isValidSudoku(arr))

