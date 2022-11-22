# 병사 배치하기
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.reverse()

# 1차원으로 리스트 초기화
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
