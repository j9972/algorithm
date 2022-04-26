import sys
input = sys.stdin.readline

# d를 모두 1으로 두고 a를 통해 증가 감소를 찾아서 숫자를 증가시키는 방향으로
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    re_a = a[::-1]

    increasedp = [1] * n
    decreasedp = [1] * n
    res = [0] * n

    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                increasedp[i] = max(increasedp[i], increasedp[j]+1)
            if re_a[i] > re_a[j]:
                decreasedp[i] = max(decreasedp[i], decreasedp[j]+1)

# -1을 해주는 이유는 중복되는 수를 빼주는것
# 12345 / 521 증가와 감소를 보면 5가 중복이 된다
    for i in range(n):
        res[i] = increasedp[i] + decreasedp[n-i-1] - 1

    print(max(res))
