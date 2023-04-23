import sys
input = sys.stdin.readline

def solution(s):
    ans = len(s)

    for step in range(1,len(s)//2+1):
        compress = ""
        prev = s[:step]
        cnt = 1
        for i in range(step,len(s),step):
            if prev == s[i:i+step]:
                cnt += 1
            else:
                compress += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = s[i:i+step]
        compress += str(cnt) + prev if cnt >= 2 else prev
        ans = min(ans,len(compress))

    return ans
print(solution('aabbaccc'))
