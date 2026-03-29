import sys
input = sys.stdin.readline

state = input().split('-')

ans = 0
for i in range(len(state)):
    val = state[i].split('+')

    temp = 0
    for j in val:
        temp += int(j)
    
    if i == 0:
        ans += temp
    else:
        ans -= temp

print(ans)
