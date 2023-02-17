def solution(s):
    ans = len(s)
    for step in range(1, len(s)//2+1):
        prev = s[:step]
        cnt = 1
        res = ""

        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                cnt += 1
            else:
                res += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = s[i:i+step]
        res += str(cnt) + prev if cnt >= 2 else prev
        ans = min(ans, len(res))

    return ans


print(solution("abcabcabcabcdededededede"))  # 14
