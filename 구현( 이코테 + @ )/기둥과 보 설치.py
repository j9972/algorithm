def possible(ans):
    for x,y,frame in ans:
        if frame ==0:
            if y == 0 or [x-1,y,1] in ans or [x,y,1] in ans or [x,y-1,0] in ans:
                continue
            return False
        elif frame == 1:
            if([x-1,y,1] in ans and [x+1,y,1] in ans) or [x,y-1,0] in ans or [x+1,y-1,0] in ans:
                continue
            return False
    return True

def solution(n, build_frame):
    ans = []
    for frame in build_frame:
        x,y,build,oper = frame
        if oper == 1:
            ans.remove([x,y,build])
            if not possible(ans):
                ans.append([x,y,build])
        elif oper == 0:
            ans.append([x,y,build])
            if not possible(ans):
                ans.remove([x,y,build])

    return sorted(ans)