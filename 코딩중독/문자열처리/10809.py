
arr = input()
counting = [-1] * 26

for i in range(len(arr)):
    if counting[ord(arr[i]) - 97] != -1:
        continue
    else:
        counting[ord(arr[i]) - 97] = i

for i in range(26):
    print(counting[i], end=' ')
