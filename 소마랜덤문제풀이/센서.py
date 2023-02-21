#골드 5 - 2212
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
sensor.sort()

diff = [sensor[i] - sensor[i-1] for i in range(1,n)]
diff.sort()

print(sum(diff[:n-k]))