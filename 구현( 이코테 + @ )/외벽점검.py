from itertools import permutations as pm
def solution(n, weak, dist):
    ans = len(dist) + 1
    
    dist.sort(reverse=True)
    length = len(weak)
    
    for i in range(length):
        weak.append(weak[i]+n)
    
    for st in range(length):
        for friends in list(pm(dist, len(dist))):
            cnt = 1
            pos = weak[st] + friends[cnt-1]
            
            for idx in range(st, st+length):
                if weak[idx] > pos:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    pos = weak[idx] + friends[cnt-1]
            ans = min(ans, cnt)
    if ans > len(dist):
        return -1
    
    return ans