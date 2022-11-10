# 문자열 압축
import sys
input = sys.stdin.readline

# s는 시작시 '\n' 이 있음
s = input()

length = len(s)

# 간격을 기준으로 해서 비교를 해야한다
for step in range(1, len(s)//2 + 1):
    count = 1
    sentense = ""
    prevStep = s[0:step]

    for nextStep in range(step, len(s), step):
        if prevStep == s[nextStep:nextStep+step]:
            count += 1
        else:
            sentense += str(count) + prevStep if count >= 2 else prevStep
            prevStep = s[nextStep:nextStep+step]
            count = 1
    sentense += str(count) + prevStep if count >= 2 else prevStep
    length = min(length, len(sentense))

print(length - 1)
