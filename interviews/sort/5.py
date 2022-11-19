
def solution(A):
    event_point = []

    for e_start, e_end in A:
        event_point.append((e_start, 0))
        event_point.append((e_end, 1))
    
    event_point.sort() # 정렬해줌. 단, 같은 경우 시작점이 끝점보다 앞에 오도록
    
    maxNumSimultaneousEvents = 0
    numSimultaneousEvents = 0

    for _, e_type in event_point:
        if e_type == 0:
            numSimultaneousEvents += 1
            maxNumSimultaneousEvents = max(maxNumSimultaneousEvents, numSimultaneousEvents)
        else:
            numSimultaneousEvents -= 1
    
    return maxNumSimultaneousEvents


if __name__ == "__main__":
    # 각 원소마다 이벤트 시작, 끝 이다. 
    A = [(1, 5), (6, 10), (11, 13), (14, 15), (2, 7), (8, 9), (12, 15), (4, 5), (9, 17)]
    print(solution(A))