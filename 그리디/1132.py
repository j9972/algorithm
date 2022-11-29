n = int(input())
arr = [[0, 'A'], [0, 'B'], [0, 'C'], [0, 'D'], [0, 'E'],
       [0, 'F'], [0, 'G'], [0, 'H'], [0, 'I'], [0, 'J']]

first = [0 for _ in range(10)]

for i in range(n):
    word = input()
    size = len(word)
    for j in range(size):
        # 65는 ord('A') 값 => word를 순차적으로 해서 idx를 구한다
        idx = ord(word[size-j-1]) - 65
        if j == size - 1:
            first[idx] = 1
        arr[idx][0] += 10**j  # 계수를 구해서 더해준다

arr.sort(reverse=True)  # 내림차순

if arr[9][0] != 0:  # 내림차순 정렬된 배열의 마지막 원소의 값이 0이 아니라면 모든 알파벳 사용한것
    for i in range(9, -1, -1):  # 거꾸로 구해간다
        if first[ord(arr[i][1]) - 65] == 0:  # first에 들어있는지 체크
            temp = list(arr[i])
            arr.remove(temp)
            arr.append(temp)
            break

res = 0
for i in range(10):
    res += arr[i][0] * (9-i)  # 계수 * (9-i)
print(res)
