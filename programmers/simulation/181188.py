def solution(targets):
    answer = 0
    
    # 일단 정렬을 먼저 (s, e 오름차순)
    targets.sort()
    # print(targets)
    
    idx = 0
    while idx < len(targets):
        
        s, e = targets[idx]
        iidx = 1
        
        # 다음 미사일이 요격가능한지 판단
        while idx + iidx < len(targets):
            ss, ee = targets[idx + iidx]
            
            if e > ss: # 처음 미사일에 e보다 다음 미사일의 ss가 더 작다면 요격 가능
                iidx += 1
                e = min(e, ee) # 중요!!!
            else:
                break
        
        answer += 1
        idx += iidx
    
    return answer