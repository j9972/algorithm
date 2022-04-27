
n = list(input())
stack = []
ans = 0

for i in range(len(n)):
    if n[i] == '(':
        stack.append('(')
    else:
        if n[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1

print(ans)
