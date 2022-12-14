# 재정렬
import sys
input = sys.stdin.readline

s = input().rstrip()


def solution(s):
    res = len(s)

    for step in range(1, len(s)//2 + 1):
        cnt = 1
        ans = ""
        prev = s[0:step]

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                cnt += 1
            else:
                ans += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = s[j:j+step]
        ans += str(cnt) + prev if cnt >= 2 else prev
        res = min(len(ans), res)
    return res


print(solution(s))
