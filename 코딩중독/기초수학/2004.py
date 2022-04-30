import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 0이 끝자리라는건 10의 배수라는 의미 이다


def c_n(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count


print(min(c_n(n, 5) - c_n(m, 5) - c_n(n-m, 5),
      c_n(n, 2) - c_n(m, 2) - c_n(n-m, 2)))
