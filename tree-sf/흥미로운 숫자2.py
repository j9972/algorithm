from collections import Counter

x,y= map(int,input().split())

# cnt = 0
# for i in range(x,y+1):
#     counter = Counter(list(str(i)))

#     if len(dict(counter)) != 2:
#         continue
    
#     one_cnt = 0 
#     for j in dict(counter).values():
#         if j == 1:
#             one_cnt += 1
    
#     if one_cnt == 1:
#         cnt += 1
# print(cnt)

cnt = 0
    
for i in range(x,y+1):
    num = i
    digit = [0] * 10
    all_digits = 0

    while num:
        digit[num % 10] += 1
        all_digits += 1
        num //= 10
    
    flag = False

    for j in range(10):
        if digit[j] == all_digits - 1:
            flag = True
    
    if flag:
        cnt += 1
print(cnt)