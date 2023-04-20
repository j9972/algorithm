import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())

    ppl = []
    for i in range(n):
        paper,interview = map(int,input().split())
        ppl.append([paper,interview])
    ppl.sort(key=lambda x:(x[0], x[1]))

    res = 1
    top = 0
    p = len(ppl)
    for i in range(1,p):
        if ppl[i][1] < ppl[top][1]:
            top = i
            res += 1

    print(res)