# 더이상 풀지 말기
import sys
input = sys.stdin.readline

n = int(input())

# 숫자를 리스트로 넣는 방법
array = list(map(int, str(n)))
left = []

while True:
    if len(array) == len(left):
        break
    left.append(array.pop(0))

if sum(array) == sum(left):
    print("LUCKY")
else:
    print("READY")
