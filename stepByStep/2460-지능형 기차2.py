arr = [
    tuple(map(int,input().split()))
    for _ in range(10)
]

max_ppl, current = 0, 0

for o, i in arr:
    current -= o 
    current += i

    max_ppl = max(max_ppl, current)

print(max_ppl)

