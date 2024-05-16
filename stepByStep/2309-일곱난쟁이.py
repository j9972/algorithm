from itertools import combinations as cb

arr = [
    int(input())
    for _ in range(9)
]

tot = sum(arr)
non_seven = list(cb(arr, 2))

for i in non_seven:
    if tot - sum(i) == 100:
        for j in sorted(arr):
            if j not in i:
                print(j)
        break

#print(non_seven)

# for i in range(8):
#     tot -= arr[i]
#     for j in range(i+1, 9):
#         tot -= arr[j]

#         if tot == 100:
#             non_seven.append(arr[i])
#             non_seven.append(arr[j])
#             break
    
#         tot += arr[j]
    
#     if tot == 100:
#         break

#     tot += arr[i]

# for i in sorted(arr):
#     if i not in non_seven:
#         print(i)
    