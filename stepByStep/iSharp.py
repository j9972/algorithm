iSharp = list(map(str, input().split()))

iSharp_list = []

for i in range(1,len(iSharp)):

    var = ''
    temp = iSharp[0]
    idx = 0

    for j in range(len(iSharp[i]) - 1):
        if not iSharp[i][j] in ['[',']','*','&']:
            var += iSharp[i][j]
            idx = j
        else:
            break

    for j in iSharp[i][idx+1:-1][::-1]:
        if j == ']':
            continue
        elif j == '[':
            temp += '[]'
        else:
            temp += j

    temp += ' ' + var

    iSharp_list.append(temp)

for i in iSharp_list:
    print(i+';')
