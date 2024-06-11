string = input()

tmp, ans, basket = 1,0,[]

for i in range(len(string)):
    if string[i] == '(':
        tmp *= 2
        basket.append(string[i])
    
    elif string[i] == '[':
        tmp *= 3
        basket.append(string[i])
    
    elif string[i] == ')':
        if not basket or basket[-1] == '[':
            ans = 0
            break
        if string[i-1] == '(':
            ans += tmp
        
        tmp //= 2
        basket.pop()

    elif string[i] == ']':
        if not basket or basket[-1] == '(':
            ans = 0
            break
        if string[i-1] == '[':
            ans += tmp
        
        tmp //= 3
        basket.pop()

if basket:
    print(0)
else:
    print(ans)