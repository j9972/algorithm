testNum = int(input())

for i in range(testNum):
    a, b = map(int, input().split())
    print('Case #{}: {}'.format(i+1, a+b))
