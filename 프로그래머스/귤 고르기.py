# dict()을 사용한 방법
def solution(k, t):
    cnt = 0
    ans = 0
    
    dic = {}
    for i in t:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    
    for i in sorted_dic:
        cnt += i[1]
        ans += 1
        if cnt >= k:
            break
    
    return ans

# dict()을 쓰지 않고 Counter() 사용해서 풀기
import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer