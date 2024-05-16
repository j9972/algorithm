from itertools import combinations as cb

arr = [
    int(input())
    for _ in range(9)
]

tot = sum(arr)
non_seven = list(cb(arr, 2))

for i in non_seven:
    if tot - sum(i) == 100:
        for j in sorted(arr):
            if j not in i:
                print(j)
        break