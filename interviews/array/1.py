def solution(arr, pivot_idx):
    pivot = arr[pivot_idx]

    # 첫번째 단계. 피벗보다 작은 원소는 왼쪽으로 이동시킴
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[smaller], arr[i] = arr[i], arr[smaller]
            smaller += 1
    
    # 두번째 단계. 피벗보다 큰 원소는 오른쪽으로 이동시킴
    larger = len(arr) - 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > pivot:
            arr[larger], arr[i] = arr[i], arr[larger]
            larger -= 1
    
    return arr


def solution2(arr, pivot_idx):
    pivot = arr[pivot_idx]

    # 0~smaller : 피벗보다 작은 그룹
    # smaller~equal : 피벗과 같은 그룹
    # equal~larger : 아직 미분류 그룹
    # larger~끝까지 : 피벗보다 큰 그룹
    smaller, equal, larger =  0, 0, len(arr)

    # 분류되지 않은 원소가 있는 동안 계속 순회
    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[larger], arr[equal] = arr[equal], arr[larger]
        print(arr, smaller, equal, larger)
    
    return arr


if __name__ == "__main__":
    arr = [0, 1, 2, 0, 2, 1, 1]
    print(solution2(arr, 3)) 