from itertools import permutations as pm

def solution(k, dungeons):
    ans = []
    
    
    all_dun = list(pm(dungeons, len(dungeons)))
    
    for d in all_dun:
        st = k
        cnt = 0
        for i in d:
            if st >= i[0]:
                st -= i[1]
                cnt += 1
        ans.append(cnt)
    return max(ans)