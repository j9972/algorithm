# 1235 실버4
import sys
input = sys.stdin.readline

nums = []
n = int(input())
for i in range(n):
    data = input().rstrip()
    nums.append(data[::-1])

cnt = 1
flag = False
for i in range(len(nums[0])):
    res = []
    check = ''
    for j in nums:
        check = j[:i+1]
        if check not in res:
            res.append(check)
            if len(set(res)) == n:
                flag = True
            #print('res :',res)
            check = ''
        else:
            cnt += 1
            break
    if flag == True:
        print(cnt)
        break
