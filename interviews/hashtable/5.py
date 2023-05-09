from collections import defaultdict


def solution(arr):
    nearest_repeated_distance = float("inf")
    word_to_index = defaultdict(str)
    for i in range(len(arr)):
        if arr[i] in word_to_index.keys():
            nearest_repeated_distance = min(nearest_repeated_distance, i - word_to_index[arr[i]])
        word_to_index[arr[i]] = i
    
    return nearest_repeated_distance

if __name__ == "__main__":
    arr = ['All', 'work', 'and', 'no', 'play', 'makes', 'for', 'no', 'work', 'no', 'fun', 'and', 'no', 'results']
    print(solution(arr)) # 정답은 두번째 no와 세번째 no 사이 거리인 2이다. 