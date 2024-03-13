import sys

n,l = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

ans = 0

# 오른쪽과 아래쪽 이동만 생각하면 된다.
dxs, dys = [0,1], [1,0]

def in_range(idx):
    return 0<=idx<n

def compare_height(val, next_val):
    if abs(val - next_val) == 1:
        return True
    else:
        return False

# 2 * n 번 돌리기 ( 순서 뒤집으면 오른, 내림 전부 점검 가능 )
def check_line(temp):

    tmp = [0] * n
    
    idx = 0
    while idx < n-1:
        #print(idx)
        if compare_height(temp[idx], temp[idx+1]):
            
            if temp[idx] > temp[idx+1]:
                tmp_val = temp[idx+1]

                if not in_range(idx+l):
                    return False

                for j in range(idx+1, idx+1+l):
                    if tmp[j] == 1:
                        return False
                    if tmp_val != temp[j]:
                        return False
                    tmp[j] = 1
            
                idx += l

            elif temp[idx] < temp[idx+1]:
                tmp_val = temp[idx]

                if not in_range(idx-l+1):
                    return False
                
                for j in range(idx, idx-l,-1):
                    if tmp[j] == 1:
                        return False
                    if tmp_val != temp[j]:
                        return False
                    tmp[j] = 1  
                
                idx += 1

        else:
            if temp[idx] == temp[idx+1]:
                idx += 1
                continue
            else:
                return False
            
    return True

res = []
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(arr[i][j])
    res.append(tmp)

for j in range(n):
    tmp = []
    for i in range(n):
        tmp.append(arr[i][j])
    res.append(tmp)

#print(res)

ans = 0
for i in res:   
    if check_line(i):
        #print(i)
        ans += 1
print(ans)