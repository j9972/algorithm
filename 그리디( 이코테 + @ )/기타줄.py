import sys
input = sys.stdin.readline

n,m = map(int,input().split())

package = []
each = []
for i in range(m):
    a,b = map(int,input().split())
    package.append(a)
    each.append(b)

mPack = min(package)
mEach = min(each)


def count(n,pack,each):
    cost = 0
    while n > 0:
        if n >= 6:
            if pack * (n//6) >= each * 6 * (n//6):
                cost += (each * n)
                break
            else:
                cost += pack * (n//6)
            n -= 6 * (n//6)
        else:
            if pack <= each * (n%6):
                cost += pack 
            else:
                cost += each * (n%6)
            n = 0
    return cost

cost = count(n,mPack,mEach)

print(cost)
