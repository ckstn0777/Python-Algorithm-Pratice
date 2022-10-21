# https://www.acmicpc.net/problem/2805
# 이진탐색 시간 복잡도 : O(log n)

'''
4 7
20 15 10 17
'''

def sum_tree(tree, mid):
    if tree - mid >= 0:
        return tree - mid
    else:
        return 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    answer = 0
    left, right = 0, max(trees)
    while left <= right:
        mid = left + ((right - left) // 2)
        st = sum(map(lambda tree: sum_tree(tree, mid), trees)) # 람다함수 이렇게 쓰면 되나? ㅋㅋ

        if st >= m:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)