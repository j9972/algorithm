def solution(sequence, k):
    length = len(sequence)
    end = 0
    interval_sum = sequence[0]
    ans = []
    
    for start in range(length):
        
        while interval_sum < k and end + 1 < length:
            end += 1
            interval_sum += sequence[end]            
        
        if interval_sum == k:
            if not ans:
                ans = [start, end]
            else:
                left, right = ans
                if end - start < right - left:
                    ans = [start, end]
        
        # 이렇게 처음 시작 위치의 값을 빼주면서 투 포인터를 이어가는거다
        interval_sum -= sequence[start]

    return ans
