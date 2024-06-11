h,w = map(int,input().split())
blocks = list(map(int,input().split()))

cur_height = blocks[0]
amount = 0
among_block = []

for i in range(w):
    flag = False
    
    if blocks[i] <= cur_height and i != 0:
        among_block.append(blocks[i])
    elif blocks[i] > cur_height:
        flag = True
        cur_height = blocks[i]

    print("blocks[i] : {}, among_block : {}".format(blocks[i], among_block))

    if i == w-1:
        flag = True
    
    if flag:
        for j in among_block:
            amount += abs(j - max(among_block))
        
        among_block = []

print(amount)
    
    