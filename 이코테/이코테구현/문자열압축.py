def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        sentense = ""
        count = 1
        prev = s[0:step]

        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                sentense += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        sentense += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(sentense))

    return answer


print(solution('asdasd'))
