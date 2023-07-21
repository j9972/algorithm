def solution(x, y, n):
    answer = 0
    
    s = set()
    s.add(x)
    
    if n > y-x and y %2 != 0 and y %3 != 0:
        return -1
    
    while s:
        if y in s:
            return answer
        
        another = set()
        for i in s:
            if i + n <= y:
                another.add(i+n)
            if i * 2 <= y:
                another.add(i*2)
            if i * 3 <= y:
                another.add(i*3)
        s = another
        answer += 1
    
    return answer

# DP

def solution(x, y, n):
    INF = int(1e9)

    d = [INF] * (y+1)
    d[x] = 0

    for i in range(x,y+1):
        if d[i] == INF:
            continue
        if i + n <= y:
            d[i+n] = min(d[i+n], d[i] + 1)
        if i * 2 <= y:
            d[i*2] = min(d[i*2], d[i] + 1)
        if i * 3 <= y:
            d[i*3] = min(d[i*3], d[i] + 1)

    if d[y] == INF:
        return -1

    return d[y]