
from collections import defaultdict

def solution(arr, t):
    arr_dict = defaultdict(int)

    for a in arr:
        arr_dict[a] = True

    for i in range(len(arr)):
        for j in range(len(arr)):
            if t - (arr[i] + arr[j]) in arr_dict.keys():
                return True
    
    return False


def solution2(arr, t):
    arr.sort()

    for a in arr:
        start, end = 0, len(arr) - 1
        while start <= end:
            if arr[start] + arr[end] < t - a:
                start += 1
            elif arr[start] + arr[end] > t - a:
                end -= 1
            else:
                return True
    
    return False


if __name__ == "__main__":
    arr = [11, 2, 5, 7, 3]
    print(solution2(arr, 22)) # 21 - true / 22 - false


