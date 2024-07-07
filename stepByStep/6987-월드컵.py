arr = [
    list(map(int,input().split()))
    for _ in range(4)
]

ans = []

matchup = [
    (0,1),(0,2),(0,3),(0,4),(0,5),
    (1,2),(1,3),(1,4),(1,5),
    (2,3),(2,4),(2,5),
    (3,4),(3,5),
    (4,5),
]

def choose(matchup_idx):

    global cnt

    if matchup_idx == 15:
        cnt = 1
        return
    
    team1, team2 = matchup[matchup_idx]
    
    for i in range(3):
        if res[team1][i] > 0 and res[team2][2-i] > 0:
            res[team1][i] -= 1
            res[team2][2-i] -= 1

            choose(matchup_idx+1)

            res[team1][i] += 1
            res[team2][2-i] += 1


for i in arr:

    res = [
        i[j * 3 : (j+1) * 3]
        for j in range(6)
    ]

    cnt = 0

    for j in range(6):
        if sum(res[j]) != 5:
            break
    else:
        choose(0)
    
    ans.append(cnt)

print(*ans)