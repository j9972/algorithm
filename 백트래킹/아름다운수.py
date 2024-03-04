n = int(input())
ans = list()

res = 0

def beautiful():
    idx = 0
    #print("ans :", ans, len(ans))
    while idx < len(ans):

        if idx + ans[idx] > len(ans):
            return False

        for i in range(idx,idx + ans[idx]):
            if ans[idx] != ans[i]:
                return False

        idx += ans[idx]

    return True

def choose(cnt):
    global res

    if cnt == n:
        if beautiful():
            res += 1
        return
    
    for i in range(1,5):
        ans.append(i)
        choose(cnt+1)
        ans.pop()

choose(0)
print(res)