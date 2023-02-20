# 실버 3 - 2852
import sys
input = sys.stdin.readline

n = int(input())

score = 0
first = 0
second = 0

for i in range(n):
    teamNum, time = input().split()
    m,s = map(int, time.split(':'))
    
    if teamNum == '1':
        score += 1
        pause_time = 0
        check_time1 = 0
        if score > 0:
            # 1팀이 이기기 시작.
            check_time1 = m*60 + s
        if score == 0:
            pause_time = m*60 + s
        first = (pause_time - check_time1)
    else:
        score -= 1
        if score < 0:
            # 2팀이 이기기 시작
            pass

print(first)
    
    
    
