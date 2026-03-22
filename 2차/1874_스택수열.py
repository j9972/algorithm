import sys
input = sys.stdin.readline

n = int(input())

number_list = []
phase_list = []
cnt = 1
flag = True

for i in range(1, n+1):
    number = int(input())

    while cnt <= number:
        number_list.append(cnt)
        phase_list.append('+')
        cnt += 1
    
    if number_list[-1] == number:
        number_list.pop()
        phase_list.append('-')
    else:
        flag = False
        break


if flag == False:
    print('NO')
else:
    for i in phase_list:
        print(i)


