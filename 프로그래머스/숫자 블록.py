# Lv - 2 "자신 외의 가장 큰 약수 찾기" 랑 같은 메커니즘
def check(n):
    if n == 1:
        return 0
    ans = [1]
    
    for i in range(2, int(n ** (1/2)) + 1):
        if (n%i == 0) and i <= 1e7:
            ans.append(i)
            if (n//i <= 1e7) and n // i != n:
                ans.append(n//i)
    
    return max(ans)

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        answer.append(check(i))
    return answer