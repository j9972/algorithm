# 더이상 풀지 말기
# import sys
# input = sys.stdin.readline

# n = int(input())

# # 숫자를 리스트로 넣는 방법
# array = list(map(int, str(n)))
# left = []

# while True:
#     if len(array) == len(left):
#         break
#     left.append(array.pop(0))

# if sum(array) == sum(left):
#     print("LUCKY")
# else:
#     print("READY")

# 럭키 스트레이트
import sys
input = sys.stdin.readline

n = int(input())

n_list = list(map(int, str(n)))

left = n_list[:len(n_list)//2]
right = n_list[len(n_list)//2:]

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')
