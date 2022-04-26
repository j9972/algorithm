# 국어는 내림 차순
# 영어는 오름 차순
# 수학은 내림 차순
# 다 같으면 이름이 사전으로 순서
import sys
n = int(sys.stdin.readline())
data = []

for i in range(n):
    name, kor, eng, mat = map(str, sys.stdin.readline().split())
    data.append((name, int(kor), int(eng), int(mat)))

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in data:
    print(i[0])
