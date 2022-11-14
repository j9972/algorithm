# 큰수의 법칙
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

ans = 0

# 나눠지는 경우 k+1은 수열의 길이, m을  k+1로 나눠지는 값은 덩어리의 개수, *k 를 하면서 총 큰값이 나오는 회수
res = int(m/(k+1)) * k

# 나눠지지 않는 경우
res += m % (k+1)

ans = res * data[0]
ans += (m-res) * data[1]

print(ans)
