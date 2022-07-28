import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0

# bin 함수는 2잔수로 버꿔준다
while bin(n).count('1') > k:  # bin(N)에서 1의 개수 = 총 물병의 개수
    n += 1
    count += 1

print(count)  # 사야하는 물병수

# 1리터씩 있는 물병을 한번에 k개를 옮길 수 있다. ( k개를 넘지 않는 비어이 ㅆ지 않은 물병을 만들려함 )

# 병을 같은 무게끼리만 (한쪽에 있는 묿병을 다른 한쪽으로 옮긴다 ) 합칠 수 있다는 말은 2의 제곱승인 숫자들의 합으로 이루어져 있다
#  최종 물병 수가 k보다 크게 되면 n에 1을 더해서 다시 이진수로 표현해서 1의 개수를 세면 된다
