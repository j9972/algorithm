# 실버 2 - 11501
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    days = int(input())
    cost = list(map(int,input().split()))

    mv = 0
    money = 0

    for i in range(len(cost)-1,-1,-1):
        if cost[i] > mv:
            mv = cost[i]
        else:
            money += mv - cost[i]
    print(money)


    # money = 0

    # def check(cost):
    #     global money
    #     maxValue = max(cost)
    #     cnt = 0
    #     mid = 0
    #     for i in range(days):
    #         if cost[i] != maxValue:
    #             mid -= cost[i]
    #             cnt += 1
    #         else:
    #             if cnt != 0:
    #                 money += cnt * maxValue + mid
    #                 cnt = 0
    #                 mid = 0
    #                 if cost[i] == cost[-1]:
    #                     return money
    #                 else:
    #                     check(cost[i+1:])
    #             else:
    #                 money += 0

    #             return money
    # print(check(cost))
                
    
