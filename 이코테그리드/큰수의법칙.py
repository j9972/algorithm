import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

res = 0
while m > 0:
    for i in range(k):
        res += num_list[-1]
        m -= 1
    res += num_list[-2]
    m -= 1

print(res)


# way2 ( 시간초과 - 반복되는 수열 찾기 )
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

# m을 k+1(반복되는 수열 길이) 나눈 몫이 수열이 반복되는 횟수 * k = 가장 큰 수가 등장하는 횟수
count = int(m/(k+1)) * k
count += m % (k+1)  # k+1 로 나뉘어 지지 않은 경우

res = 0
res += count * num_list[-1]
res += (m-count) * num_list[-2]
print(res)
