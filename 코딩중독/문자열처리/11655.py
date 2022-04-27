import sys
input = sys.stdin.readline

arr = input()
ans = ' '

for i in arr:
    if 'a' <= i <= 'z':
        i = ord(i) + 13
        if i > 122:
            i -= 26
        ans += chr(i)
    elif 'A' <= i <= 'Z':
        i = ord(i) + 13
        if i > 90:
            i -= 26
        ans += chr(i)
    else:
        ans += i

print(ans)
