d = [1] * 10001

# for i in range(2,10001):
#     d[i] += d[i-2]
# for i in range(3,10001):
#     d[i] += d[i-3]

# for tc in range(int(input())):
#     n = int(input())

#     print(d[n])


for j in range(2,4):
    for i in range(1, len(d)):
        if i >= j:
            d[i] = d[i] + d[i-j]

 
for tc in range(int(input())):
    n = int(input())

    print(d[n])           