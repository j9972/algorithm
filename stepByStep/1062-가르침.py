n,k = map(int,input().split())

words = [
    input()[4:-4]
    for _ in range(n)
]

alpha = ['a', 'n', 't', 'i', 'c']
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
            'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

max_val = 0

def choose(n, start):
    global max_val

    if n == 0:
        max_val = max(max_val, calc())
        return
    
    for i in range(start, len(alpha_list)):
        if alpha_list[i] not in alpha:
            alpha.append(alpha_list[i])
            choose(n-1, i+1)
            alpha.pop()
    
def calc():
    res = 0

    for i in words:
        flag = True

        for j in i:
            if j not in alpha:
                flag = False
                break

        if flag:
            res += 1
    return res


if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    choose(k-5, 0)
    print(max_val)