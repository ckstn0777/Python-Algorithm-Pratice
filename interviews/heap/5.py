
import heapq

def solution(arr):
    min_heap = []
    heapq.heapify(min_heap) # 최소힙 (큰 부분 집합)
    
    max_heap = []
    heapq.heapify(max_heap) # 최대힙 (작은 부분 집합)

    result = []

    for i in range(len(arr)):
        heapq.heappush(min_heap, arr[i]) 
        heapq.heappush(max_heap, -heapq.heappop(min_heap)) # 파이썬은 기본이 최소힙이므로 최대힙일때는 (-) 부호

        # 비율을 맞춰줘야지 (최대힙이 더 크면 최소힙으로 이동시켜줌)
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(min_heap) == len(max_heap):
            result.append(0.5 * (min_heap[0] + -max_heap[0]))
        else:
            result.append(min_heap[0])

    return result


if __name__ == "__main__":
    arr = [1, 0, 3, 5, 2, 0, 1]
    print(solution(arr))