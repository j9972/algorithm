# 1205 실버4
import sys
input = sys.stdin.readline

n, taesu ,p = map(int,input().split())

if n == 0:
    print(1)
else:
    scores = list(map(int,input().split()))
    scores.append(taesu)
    scores.sort(reverse=True)
    idx = scores.index(taesu)+1

    if idx > p:
        print(-1)
    else:
        if n == p and taesu <= scores[-1]:
            print(-1)
        else:
            print(idx)
            
# ranking = []
    # for i in range(n):
    #     if scores[-1] >= taesu:
    #         scores.append(taesu)
    #         break
    #     if scores[i] < taesu:
    #         scores.insert(i,taesu)
    # #print(scores)

    # for i in range(len(scores)):
    #     cnt = 1
    #     for j in range(i+1,len(scores)):
    #         if scores[i] != scores[j]:
    #             if cnt == 1:
    #                 ranking.append(i+1)
    #                 break
    #             else:
    #                 data = ranking[-1]
    #                 for i in range(cnt):
    #                     ranking.append(data+1)
    #                 break
    #         else:
    #             cnt += 1

    #         if cnt != 1:
    #             data = ranking[-1]
    #             for i in range(cnt):
    #                 ranking.append(data+1)
    #             break



    # for rank in ranking:


    # if scores.index(taesu)+1 > p:
    #     print(-1)
    # else:
    #     print(ranking[scores.index(taesu)+1])