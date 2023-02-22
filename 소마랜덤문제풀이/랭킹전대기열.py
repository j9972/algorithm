#실버 2 - 20006
import sys
input = sys.stdin.readline

p,m = map(int,input().split())

players = []
for i in range(p):
    level, nick = input().split()
    if not players:
        players.append([[int(level), nick]])
        continue
    
    enter = False

    for player in players:
        if len(player) < m and player[0][0] - 10 <= int(level) <= player[0][0] + 10:
            enter = True
            player.append([int(level), nick])
            break

    if not enter:
        players.append([[int(level), nick]])
    
for player in players:
    player.sort(key=lambda x : x[1])

for i in players:
    if len(i) == m:
        print('Started!')
    else:
        print('Waiting!')
    for level, nick in i:
        print(level,nick)