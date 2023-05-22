# 2504 실버1
import sys
input = sys.stdin.readline

p = input().rstrip()

st = []
tmp = 1
res = 0

for i in range(len(p)):
    if p[i] == '(':
        st.append(p[i])
        tmp *= 2
    elif p[i] == '[':
        st.append(p[i])
        tmp *= 3
    elif p[i] == ')':
        if not st or st[-1] == '[':
            res = 0
            break
        if p[i-1] == '(':
            res += tmp
        st.pop()
        tmp //= 2
    elif p[i] == ']':
        if not st or st[-1] == '(':
            res = 0
            break
        if p[i-1] == '[':
            res += tmp
        st.pop()
        tmp //= 3
if st:
    print(0)
else:
    print(res)
