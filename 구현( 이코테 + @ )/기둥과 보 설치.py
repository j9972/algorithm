def possible(arr):
    for x,y,frame in arr:
        if frame == 0: # 기둥
            if (y == 0) or [x,y-1,0] in arr or [x-1,y,1] in arr or [x,y,1] in arr:
                continue
            return False
        elif frame == 1: # 보
            if [x+1,y-1,0] in arr or ([x+1,y,1] in arr and  [x-1,y,1] in arr) or [x, y-1, 0] in arr:
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x,y,a,oper = frame
        if oper == 0: # 삭제
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
        elif oper == 1: # 설치
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a])
    
    return sorted(answer)