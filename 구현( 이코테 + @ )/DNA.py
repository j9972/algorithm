#1969 실버4
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dna = []
for i in range(n):
    dna.append(input().rstrip())

ans = ''
cnt = 0

# 가로 -> 세로 순서로 체크
for i in range(m):
    arr = {'A':0, 'C':0, 'G':0, 'T':0}
    for j in range(n):
        if dna[j][i] in arr.keys():
            arr[dna[j][i]] += 1
    max_key = max(arr, key=arr.get)
    ans += max_key
    cnt += (n-arr[max_key])
    #print('max_key :', max_key, 'ans : ', ans, 'cnt :',cnt)
print(ans)
print(cnt)

