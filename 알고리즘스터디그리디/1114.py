l, k, c = map(int, input().split())
data = list(map(int, input().split()))

size = []
box = []

for _ in range(k):
    l = l
    for i in data:
        size.append(l-i)
        l -= i


for j in data:
    maxLPoint = j
    maxL = size[0]

    for i in range(1, len(size)):
        if maxL < size[i]:
            maxL = size[i]
            maxLPoint = data[i]
        box.append([maxL, maxLPoint])

print("box = {}".format(box))
print("box = {}".format(box[0]))


#print(maxL, maxLPoint)
