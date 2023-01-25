def solution(s):
    length = len(s)
    for step in range(1, len(s)//2 + 1):
        cnt = 1
        ans = ""
        prev = s[:step]

        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                cnt += 1
            else:
                ans += str(cnt) + prev if cnt >= 2 else prev
                cnt = 1
                prev = s[i:i+step]
        ans += str(cnt) + prev if cnt >= 2 else prev
        length = min(len(ans), length)

    return length


print(solution("ababcdcdababcdcd"))  # 9 가 정답
