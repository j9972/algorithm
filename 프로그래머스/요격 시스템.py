# 개구간의 끝 지점을 기준으로 한 요격
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    temp = 0
    for i in targets:
        if i[0]<temp:
            continue
        else:
            answer+=1
            temp = i[1]

    return answer

def solution(targets):
    # target 사이에 겹치는 부분에 대해서 미사일의 개수를 증가시키면 된다.
    
    shot, overlap = 0, {'s' : 0, 'e' : 0}
    
    for s,e in sorted(targets):
        if overlap['e'] <= s:
            shot += 1
            overlap = {'s' : s, 'e' : e}
        else:
            overlap = {'s' : max(overlap['s'],s), 'e' : min(overlap['e'],e)}
    
    return shot 