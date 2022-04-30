n = int(input())


def fact(n):
    res = 1
    if n > 0:
        res = n * fact(n-1)
    return res


print(fact(n))
