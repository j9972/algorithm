import sys
input = sys.stdin.readline

x, y = map(int, input().split())
data = [[1, 31],
        [2, 28],
        [3, 31],
        [4, 30],
        [5, 31],
        [6, 30],
        [7, 31],
        [8, 31],
        [9, 30],
        [10, 31],
        [11, 30],
        [12, 31]]

DAYS = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

tot = 0
for i in range(0, x-1):
    tot += data[i][1]
tot += y
print(DAYS[tot % 7])

# if tot % 7 == 0:
#     print('MON')
# if tot % 7 == 1:
#     print('TUE')
# if tot % 7 == 2:
#     print('WED')
# if tot % 7 == 3:
#     print('THU')
# if tot % 7 == 4:
#     print('FRI')
# if tot % 7 == 5:
#     print('SAT')
# if tot % 7 == 6:
#     print('SUN')
